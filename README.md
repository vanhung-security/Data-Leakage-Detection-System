# 🛡️ Data Leakage Detection System (DLDS)

Dự án này là hệ thống giám sát và phát hiện rò rỉ dữ liệu nội bộ (DLP) dựa trên nền tảng **Wazuh SIEM**, **Sysmon** và **Python Detection Engine**. Dự án tập trung vào việc nhận diện sớm các hành vi truy cập trái phép, sao chép dữ liệu nhạy cảm ra thiết bị ngoại vi hoặc tải lên các nền tảng đám mây trái quy định.

## 🏗️ Kiến trúc Hệ thống

Hệ thống được thiết kế theo mô hình 4 lớp, đảm bảo khả năng giám sát tập trung và phản ứng tức thời:

1. **Endpoint Layer**: Sử dụng Sysmon để thu thập các log chi tiết về tiến trình, mạng và tương tác Clipboard trên máy trạm Windows.
2. **Security Monitoring Layer**: Wazuh Manager đóng vai trò tập trung log, xử lý sự kiện và cung cấp Dashboard giám sát.
3. **Detection Layer**: Bộ não phân tích (Python Engine) thực hiện đối chiếu từ khóa nhạy cảm, mã băm (Hash) và tương quan hành vi.
4. **Database Layer**: Lưu trữ cấu hình từ khóa, thông tin máy trạm và nhật ký cảnh báo (Alerts History).

## 🚀 Tính năng chính

* **Phát hiện rò rỉ đa kênh**: Giám sát hành vi copy dữ liệu qua USB, upload lên Cloud, Email, và các ứng dụng chat.
* **Giám sát Clipboard**: Ghi nhận nội dung người dùng sao chép (Copy/Paste) để ngăn chặn rò rỉ dữ liệu qua bộ nhớ tạm.
* **Cảnh báo thời gian thực**: Tích hợp **Telegram Bot** để gửi thông báo ngay lập tức khi phát hiện hành vi đáng ngờ.
* **Phân tích tương quan**: Engine không chỉ phát hiện từ khóa đơn lẻ mà còn dựa trên sự kết hợp hành vi (vd: mở file nhạy cảm + mở trình duyệt).

## 🛠 Tech Stack

| Thành phần | Công nghệ |
| :--- | :--- |
| **SIEM** | Wazuh Manager v4.x |
| **Endpoint Monitoring** | Sysmon, Wazuh Agent |
| **Detection Engine** | Python 3.x (Requests, Watchdog, Psutil) |
| **Database** | MySQL |
| **Notification** | Telegram Bot API |
| **Automation** | Bash Scripts, PowerShell |

## 📂 Cấu trúc Dự án

```text
/
├── config/             # Cấu hình hệ thống
│   ├── ossec.conf
│   ├── sysmonconfig.xml
│   └── local_rules.xml
├── detection-engine/   # Engine phân tích log
│   ├── detection.py
│   ├── keywords.txt
│   └── requirements.txt
├── database/           # Quản lý dữ liệu
│   └── schema.sql
├── scripts/            # Script tự động hóa
│   ├── install.sh
│   └── clipboard.ps1
├── docs/               # Tài liệu dự án
│   └── Architecture.md
├── .gitignore
├── LICENSE
└── README.md
🛠 Hướng dẫn Triển khai nhanh
Cài đặt Engine:

Bash
cd scripts && sudo ./install.sh
Cấu hình: Cập nhật TELEGRAM_TOKEN và CHAT_ID vào môi trường của bạn.

Chạy giám sát:

Bash
python3 detection-engine/detection.py
🧹 Clean Up
Để ngắt kết nối và dừng giám sát:

Bash
# Dừng các process detection
pkill -f detection.py

# Xóa các file log tạm
rm /var/ossec/logs/dlp_alerts.log
Author: VanHung

## 🎥 Video Demo
Dưới đây là video demo quá trình hệ thống phát hiện rò rỉ dữ liệu và cảnh báo qua Telegram:

[▶️ XEM VIDEO DEMO TẠI ĐÂY](https://drive.google.com/file/d/1DyQebckkXhr6VR7_M98FL9qpKi1S3DJg/view?usp=sharing)
