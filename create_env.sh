#!/bin/bash
cd ..
python3 -m venv Chess_env
source Chess_env/Scripts/activate
cd Chess-AI
pip install -r requirements.txt