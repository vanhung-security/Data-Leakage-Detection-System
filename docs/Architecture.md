# Kiến trúc hệ thống giám sát rò rỉ dữ liệu (DLP)

Hệ thống được thiết kế theo mô hình 4 lớp để đảm bảo khả năng giám sát toàn diện:

## 1. Các lớp thành phần
* **Endpoint Layer**: Máy Windows cài đặt Sysmon và Wazuh Agent để thu thập log hoạt động.
* **Security Monitoring Layer**: Wazuh Manager tập trung xử lý log và hiển thị trên Dashboard.
* **Detection Layer**: Python Engine thực hiện phân tích nội dung, đối chiếu từ khóa và tính điểm rủi ro.
* **Database Layer**: Lưu trữ danh sách từ khóa nhạy cảm, mã băm (Hash) và lịch sử cảnh báo.

## 2. Luồng hoạt động
1. Người dùng thao tác (Copy, Upload, Chụp màn hình).
2. Sysmon ghi nhận log sự kiện.
3. Wazuh Agent chuyển log về Manager.
4. Detection Engine phân tích log thời gian thực.
5. Cảnh báo gửi về Telegram Bot và Dashboard nếu phát hiện hành vi vi phạm.
