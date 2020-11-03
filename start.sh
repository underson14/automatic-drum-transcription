#!/bin/bash
apt-get install python3-venv
echo "Checking Python version..."

if command -v python3 &>/dev/null; then
    echo "Found Python 3"
    python3 -m venv ./venv


    if [ $? -eq 0 ]; then
        echo OK
        source venv/bin/activate
        pip install --upgrade pip
        pip install numba==0.43.0 --user
        pip install llvmlite==0.32.1 --user
        pip install -r /content/automatic-drum-transcription/requirements.txt
        python3 /content/automatic-drum-transcription/src/start.py --folder=$1
    else
        echo "Could not execute python -m venv ./venv"
        echo "Edit the script. Change the 'python' command to the one calling python3."
    fi

else
    echo "Python 3 is not installed."
    echo "Aborting"
fi
