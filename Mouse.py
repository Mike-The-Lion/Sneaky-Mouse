# Auto mouse mover

import pyautogui as pag
import time
import random

# Move mouse to random location every 5 seconds
while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, duration=0.5)
    time.sleep(5)

# Path: Mouse.py