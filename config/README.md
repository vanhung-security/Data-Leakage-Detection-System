# Cấu hình hệ thống (Configuration)

Thư mục này chứa các tệp cấu hình cần thiết để triển khai hệ thống giám sát và phát hiện rò rỉ dữ liệu.

## Danh sách tệp tin
* `ossec.conf`: Tệp cấu hình chính cho Wazuh Agent, bao gồm thiết lập kết nối tới Wazuh Manager, danh sách các tệp log cần theo dõi (`localfile`) và cấu hình `syscheck`.
* `sysmonconfig.xml`: Tệp cấu hình Sysmon chi tiết, tập trung vào việc giám sát các sự kiện như khởi tạo tiến trình, kết nối mạng và tương tác tệp tin.
* `local_rules.xml`: Bộ quy tắc (rules) tùy chỉnh cho Wazuh, giúp phát hiện và cảnh báo các hành vi nghi ngờ như copy dữ liệu vào USB hoặc tải lên đám mây.

## Hướng dẫn sử dụng
1. **Wazuh Agent (`ossec.conf`)**:
   - Đảm bảo địa chỉ IP `10.13.3.203` là địa chỉ của Wazuh Manager.
   - Sau khi thay đổi, hãy khởi động lại Wazuh Agent: `Restart-Service wazuh` (trên PowerShell quyền Administrator).

2. **Sysmon (`sysmonconfig.xml`)**:
   - Để áp dụng cấu hình mới: `sysmon64.exe -c sysmonconfig.xml`.

3. **Wazuh Rules (`local_rules.xml`)**:
   - Di chuyển tệp này vào đường dẫn `/var/ossec/etc/rules/` trên Wazuh Manager và khởi động lại dịch vụ `wazuh-manager`.
