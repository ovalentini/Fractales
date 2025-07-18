@echo off
echo Microsoft Edge doit etre ouvert...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "function RefreshEdgePage { $edgeProcess = Get-Process -Name msedge -ErrorAction SilentlyContinue; if ($edgeProcess) { $edgeWindow = Get-Process -Name msedge | Where-Object { $_.MainWindowTitle -ne '' } | Select-Object MainWindowTitle -First 1; if ($edgeWindow) { $wshell = New-Object -ComObject WScript.Shell; $wshell.AppActivate($edgeWindow.MainWindowTitle); Start-Sleep -Seconds 1; $wshell.SendKeys('^%{F5}') } else { Write-Host 'Impossible de trouver la fenêtre Edge.' } } else { Write-Host 'Microsoft Edge n''est pas en cours d''exécution.' } }; RefreshEdgePage"
pause
