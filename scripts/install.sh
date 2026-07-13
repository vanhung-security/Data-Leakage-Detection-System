#!/bin/bash
echo "[*] Updating system and installing dependencies..."
sudo apt update && sudo apt install -y python3-pip
echo "[*] Installing Python libraries..."
pip3 install requests watchdog psutil
echo "[+] Setup complete. Please configure your .env file with TELEGRAM_TOKEN and CHAT_ID."
