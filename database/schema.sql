-- Tạo database cho hệ thống DLP
CREATE DATABASE IF NOT EXISTS dlp_system;
USE dlp_system;

-- 1. Bảng lưu trữ danh sách từ khóa nhạy cảm
CREATE TABLE keywords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    keyword_text VARCHAR(255) NOT NULL,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bảng lưu trữ thông tin các máy trạm (Agents)
CREATE TABLE agents (
    agent_id VARCHAR(50) PRIMARY KEY,
    agent_name VARCHAR(100),
    ip_address VARCHAR(45),
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Bảng lưu trữ lịch sử cảnh báo (Alerts)
CREATE TABLE alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_id VARCHAR(50),
    keyword_detected VARCHAR(255),
    destination VARCHAR(100), -- Ví dụ: Google Drive, Email, Zalo
    severity_level INT,       -- Mức độ nguy hiểm
    alert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

-- Thêm dữ liệu mẫu ban đầu
INSERT INTO keywords (keyword_text, category) VALUES 
('salary', 'Finance'),
('password', 'Security'),
('api_key', 'Security'),
('confidential', 'General'),
('cmnd', 'PII');
