from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# 355 517
time.sleep(2)
print('started')


def is_beer(g):
    return (20 <= g <= 150)


def move_it(x):
    r, g, b = picture.getpixel((x, 0))

    if is_beer(g):
        print('Found One!!')
        win32api.SetCursorPos((378+x, 609))


def worker(picture, width, height):
    pass_bubble = 0
    go = True
    back = False

    if go:
        for x in range(width):
            move_it(x)
        go = False
        back = True
    if back:
        for x in range(width-1, -1, -1):
            move_it(x)
        go = True
        back = False


while keyboard.is_pressed('q') == False:
    width = 460
    height = 1
    picture = pyautogui.screenshot(region=(378, 608, width, height))

    worker(picture, width, height)
