@echo off

call %~dp0venv/Scripts/activate

cd %~dp0main

python main.py

hide
