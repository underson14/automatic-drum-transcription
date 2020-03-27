@echo off
IF NOT EXIST ./venv (
    python3 -m venv ./venv
)
call ./venv/Scripts/activate.bat
pip install --upgrade pip
pip install -r requirements.txt
python3 ./src/start.py --folder=%1