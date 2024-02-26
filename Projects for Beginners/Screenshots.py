#!/usr/bin/env python
#Screenshots
#Github: mammaddrik

#::::: Library :::::
import os
try:
    import pyautogui
except:
    os.system("pip install pyautogui")

im = pyautogui.screenshot()
im.save("SS1.jpg")