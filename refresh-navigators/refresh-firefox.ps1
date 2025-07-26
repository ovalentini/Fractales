$log = "refresh_log.txt"
$timestamp = Get-Date -Format "dd/MM/yyyy HH:mm:ss"

$f = Get-Process firefox -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowTitle -ne '' } | Select-Object -First 1

if ($f) {
    $ws = New-Object -ComObject WScript.Shell
    $ws.AppActivate($f.MainWindowTitle)
    Start-Sleep -Milliseconds 500
    $ws.SendKeys('^{F5}')
    Add-Content -Path $log -Value "[$timestamp] [Firefox] Refresh succeeded"
} else {
    Add-Content -Path $log -Value "[$timestamp] [Firefox] Firefox not found"
}
