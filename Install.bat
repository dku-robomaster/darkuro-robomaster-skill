@echo off
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  python install.py --app codex %*
) else (
  py -3 install.py --app codex %*
)
if errorlevel 1 (
  echo Installation failed. Python 3.9 or newer is required.
  pause
  exit /b 1
)
pause
