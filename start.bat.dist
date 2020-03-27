@echo off
IF NOT EXIST ./venv (
    python -m venv ./venv
)
call ./venv/Scripts/activate.bat
pip install --upgrade pip
pip install -r requirements.txt
python ./src/start.py --folder=$1