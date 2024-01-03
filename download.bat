@echo off

:: Check for Python installation and offer options if not found
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed.
    echo.
    set /P choice="Would you like to install Python using winget? (Y/N): "
    if /I "%choice%" EQU "Y" goto install_python
) else (
    echo Python is already installed. Proceeding to install packages.
)
:: Insatll Python using Winget
winget install Python3

:: Install packages using pip
pip install -r requirements.txt
goto end

echo Installation complete.
pause