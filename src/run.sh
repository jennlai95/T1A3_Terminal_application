#! /bin/bash

python3 -m venv main-venv
source main-venv/bin/activate
pip3 install -r requirements.txt
#clear terminal
clear
#Run App
python3 main.py
