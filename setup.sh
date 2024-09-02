#!/bin/bash
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

if command_exists python3; then
    PYTHON=python3
elif command_exists python; then
    PYTHON=python
else
    echo -e "${RED}Python is not installed. Please install Python 3.x and try again.${NC}"
    exit 1
fi

PYTHON_VERSION=$($PYTHON -c 'import sys; print(sys.version_info.major)')
if [ "$PYTHON_VERSION" -ne 3 ]; then
    echo -e "${RED}Python version is not 3.x. Please install Python 3.x and try again.${NC}"
    exit 1
fi

if ! command_exists pip3 && ! command_exists pip; then
    echo -e "${RED}pip is not installed. Please install pip and try again.${NC}"
    exit 1
fi

if ! $PYTHON -c "import tkinter" &> /dev/null; then
    echo -e "${YELLOW}tkinter is not installed.${NC}"
    read -p "Would you like to install tkinter? (y/n) " choice
    case "$choice" in 
      y|Y ) 
        if [ "$(uname)" == "Darwin" ]; then
            echo -e "${BLUE}Installing tkinter for macOS...${NC}"
            brew install python-tk
        elif [ "$(uname)" == "Linux" ]; then
            echo -e "${BLUE}Installing tkinter for Linux...${NC}"
            sudo apt-get install python3-tk -y
        else
            echo -e "${RED}Please install tkinter manually for your system.${NC}"
            exit 1
        fi;;
      n|N ) 
        echo -e "${RED}tkinter is required to run the application. Exiting.${NC}"
        exit 1;;
      * ) 
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1;;
    esac
fi

echo -e "${GREEN}Creating a virtual environment...${NC}"
$PYTHON -m venv venv

echo -e "${GREEN}Activating the virtual environment...${NC}"
source venv/bin/activate

if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}Installing required packages...${NC}"
    pip install -r requirements.txt
else
    echo -e "${RED}requirements.txt not found. Please ensure the file exists.${NC}"
    deactivate
    exit 1
fi

echo -e "${GREEN}Executing moveGreater.sh...${NC}"
bash moveGreater.sh

echo -e "${GREEN}Executing moveLesser.sh...${NC}"
bash moveLesser.sh

echo -e "${GREEN}Executing main.py...${NC}"
$PYTHON main.py
