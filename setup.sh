#!/bin/bash
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

if command_exists python3; then
    PYTHON=python3
elif command_exists python; then
    PYTHON=python
else
    echo "Python is not installed. Please install Python 3.x and try again."
    exit 1
fi

PYTHON_VERSION=$($PYTHON -c 'import sys; print(sys.version_info.major)')
if [ "$PYTHON_VERSION" -ne 3 ]; then
    echo "Python version is not 3.x. Please install Python 3.x and try again."
    exit 1
fi

if ! command_exists pip3 && ! command_exists pip; then
    echo "pip is not installed. Please install pip and try again."
    exit 1
fi

echo "Creating a virtual environment..."
$PYTHON -m venv venv

echo "Activating the virtual environment..."
source venv/bin/activate

if [ -f "requirements.txt" ]; then
    echo "Installing required packages..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please ensure the file exists."
    deactivate
    exit 1
fi

echo "Executing moveGreater.sh..."
bash moveGreater.sh

echo "Executing moveLesser.sh..."
bash moveLesser.sh

echo "Executing main.py..."
$PYTHON main.py
