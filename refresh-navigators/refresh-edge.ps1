$log = "refresh_log.txt"
$timestamp = Get-Date -Format "dd/MM/yyyy HH:mm:ss"

$e = Get-Process msedge -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowTitle -ne '' } | Select-Object -First 1

if ($e) {
    $ws = New-Object -ComObject WScript.Shell
    $ws.AppActivate($e.MainWindowTitle)
    Start-Sleep -Milliseconds 500
    $ws.SendKeys('^{F5}')
    Add-Content -Path $log -Value "[$timestamp] [Edge] Refresh succeeded"
} else {
    Add-Content -Path $log -Value "[$timestamp] [Edge] Edge not found"
}


