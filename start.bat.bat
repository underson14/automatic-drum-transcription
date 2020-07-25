@echo off
python3 --version >nul 2>nul || (
	ECHO python3 wasn't found on this machine!
	WHERE python3 >nul 2>nul
	IF %ERRORLEVEL% EQU 0 (
		ECHO Opening Microsoft Store for Installation...
		python3
	)
	echo After Installation re-run this script. 
	exit 1;
)

python3.exe --version 2>nul | findstr /R /I /C:"^Python[ ]*[0-9]*[3-9]\." >nul 2>nul 
IF %ERRORLEVEL% NEQ 0 (
	echo Your Python Version is not supported! Use Python 3 or higher.
	exit 1
)

IF NOT EXIST ./venv (
    python3 -m venv ./venv
)

IF NOT EXIST ./venv/Scripts/activate.bat (
	echo Could not find ./venv/Scripts/activate.bat!
	exit 1;
)

call ./venv/Scripts/activate.bat

pip --version >nul 2>nul || (
	ECHO pip wasn't found on this machine!
	exit 1;
)

:: pip install --upgrade --user pip
python -m pip install --upgrade pip
pip install -r requirements.txt
python3 ./src/start.py --folder=%1
