@echo off
cd /d "C:\Users\Olivier\Downloads\Fractales\refresh-navigators"
setlocal enabledelayedexpansion

:MENU
cls
echo ==========================================
echo       Browser Refresh Control Panel
echo ==========================================
echo.
echo 1. Refresh Microsoft Edge
echo 2. Refresh Google Chrome
echo 3. Refresh Mozilla Firefox
echo 4. Refresh All Browsers
echo 0. Exit
echo.
set /p choix=Your choice: 

if "%choix%"=="1" call :EDGE
if "%choix%"=="2" call :CHROME
if "%choix%"=="3" call :FIREFOX
if "%choix%"=="4" (
    call :EDGE
    call :CHROME
    call :FIREFOX
    pause
)
if "%choix%"=="0" goto END
goto MENU

:EDGE
echo [Edge] Launching refresh-edge.ps1...
powershell -ExecutionPolicy Bypass -File "refresh-edge.ps1"
echo [Edge] Done.
exit /b

:CHROME
echo [Chrome] Launching refresh-chrome.ps1...
powershell -ExecutionPolicy Bypass -File "refresh-chrome.ps1"
echo [Chrome] Done.
exit /b

:FIREFOX
echo [Firefox] Launching refresh-firefox.ps1...
powershell -ExecutionPolicy Bypass -File "refresh-firefox.ps1"
echo [Firefox] Done.
exit /b

:END
echo Closing the control panel...
exit
