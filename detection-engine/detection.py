import json, time, requests, os
from datetime import datetime

# --- CẤU HÌNH ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
LOG_FILE = "/var/ossec/logs/archives/archives.json"
ALERT_FILE = "/var/ossec/logs/dlp_alerts.log"

# --- TẢI TỪ KHÓA ---
with open("keywords.txt", "r") as f:
    KEYWORDS = [line.strip().lower() for line in f]

# --- HÀM HỖ TRỢ ---
def send_telegram(message):
    if not TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try: requests.post(url, data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"})
    except: pass

def is_sensitive_file(filename):
    fname = filename.lower()
    return any(kw in fname for kw in KEYWORDS) or any(fname.endswith(ext) for ext in [".xlsx", ".docx", ".pdf", ".csv", ".sql"])

# --- ENGINE CHÍNH ---
print("[*] DLP Detection Engine Started...")
chatgpt_active = {}
gdrive_active = {}
mem_file = {}

with open(LOG_FILE, "r") as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue
        try:
            data = json.loads(line)
            now = time.time()
            agent = data.get("agent", {}).get("name", "unknown")
            full_log = json.dumps(data).lower()
            
            # 1. Phát hiện tương tác file nhạy cảm
            win_data = data.get('data', {}).get('win', {}).get('eventdata', {})
            raw_file = win_data.get('TargetFilename') or win_data.get('ArchivedSource') or ""
            
            if raw_file and is_sensitive_file(str(raw_file)):
                mem_file[agent] = {"name": raw_file, "time": now}
                print(f"[!] {agent}: Tương tác file nhạy cảm: {raw_file}")

            # 2. Phát hiện hành vi rò rỉ
            # ChatGPT
            if "chatgpt" in full_log or "openai" in full_log:
                chatgpt_active[agent] = now
            
            # 3. Correlation (Kết hợp sự kiện)
            # Nếu vừa tương tác file nhạy cảm vừa lên web thì cảnh báo
            if agent in mem_file and (now - mem_file[agent]["time"]) <= 60:
                if agent in chatgpt_active and (now - chatgpt_active[agent]) <= 60:
                    alert_msg = f"[!!!] DLP ALERT: Rò rỉ qua ChatGPT\nUser: {agent}\nFile: {mem_file[agent]['name']}"
                    print(alert_msg)
                    send_telegram(alert_msg)
                    with open(ALERT_FILE, "a") as af: af.write(alert_msg + "\n")

            # 4. Phát hiện chụp màn hình (Screenshot)
            if "snippingtool" in full_log or "100060" in full_log:
                fname = mem_file.get(agent, {}).get("name", "Unknown")
                alert_msg = f"[!!!] DLP ALERT: Phát hiện chụp màn hình dữ liệu nhạy cảm\nUser: {agent}\nFile: {fname}"
                print(alert_msg)
                send_telegram(alert_msg)
                with open(ALERT_FILE, "a") as af: af.write(alert_msg + "\n")

        except Exception as e:
            continue
