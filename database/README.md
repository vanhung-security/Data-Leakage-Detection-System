# Cấu hình hệ thống (Configuration)

Thư mục này chứa các tệp cấu hình cần thiết để triển khai hệ thống giám sát và phát hiện rò rỉ dữ liệu.

## Danh sách tệp tin
* `ossec.conf`: Tệp cấu hình chính cho Wazuh Agent, bao gồm thiết lập kết nối tới Wazuh Manager, danh sách các tệp log cần theo dõi (`localfile`) và cấu hình `syscheck`.
* `sysmonconfig.xml`: Tệp cấu hình Sysmon chi tiết, tập trung vào việc giám sát các sự kiện như khởi tạo tiến trình, kết nối mạng và tương tác tệp tin.
* `local_rules.xml`: Bộ quy tắc (rules) tùy chỉnh cho Wazuh, giúp phát hiện và cảnh báo các hành vi nghi ngờ như copy dữ liệu vào USB hoặc tải lên đám mây.
