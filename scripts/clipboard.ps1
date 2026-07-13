$path = "C:\SecurityDemo\clipboard.log"
# Kiểm tra nếu thư mục không tồn tại thì tạo mới
if (!(Test-Path "C:\SecurityDemo")) { New-Item -ItemType Directory -Path "C:\SecurityDemo" }

while($true) {
    $clip = Get-Clipboard
    if ($clip -ne $null) {
        $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $logEntry = "$date - Clipboard Content: $clip"
        Add-Content -Path $path -Value $logEntry
        Start-Sleep -Seconds 5
    }
}
