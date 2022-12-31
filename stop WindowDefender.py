import os

def turn_off():
    os.system("sc stop WinDefend")

def turn_on():
    os.system("sc start WinDefend")