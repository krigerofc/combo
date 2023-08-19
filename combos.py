import keyboard
import mouse
from time import sleep

def defesa():
    keyboard.press('space')
    sleep(5)
    keyboard.release('space')

def esquiva(valor):
    for c in range(0, valor):
        keyboard.press_and_release('q')
        sleep(0.5)
        keyboard.press_and_release('e')
        sleep(0.5)

def combo_1(quantidade):
    for c in range(0, quantidade+1):
        mouse.click(button='left')
        sleep(0.3)
        keyboard.press_and_release('e')
        sleep(0.5)
        mouse.click(button='left')
        sleep(0.3)
        keyboard.press_and_release('q')
        sleep(0.5)


def combo_2(quantidade):
    for c in range(0, quantidade+1):
        for c in range(0, 2):
            mouse.click(button='left')
            sleep(0.3)
        keyboard.press('space')
        sleep(3)
        keyboard.release('space')




def pulo(quantidade):
    for c in range(0, quantidade+1):
        keyboard.press_and_release('f')
        sleep(0.3)


def combo_super(quantidade):
    for c in range(0, quantidade + 1):
        mouse.click(button='left')
        sleep(0.3)
        keyboard.press_and_release('e')
        sleep(0.5)
        keyboard.press('space')
        sleep(3)
        keyboard.release('space')
        mouse.click(button='left')
        sleep(0.3)
        mouse.click(button='left')
        sleep(0.3)
        keyboard.press_and_release('q')
        sleep(0.5)
        mouse.click(button='left')
        sleep(0.3)
        keyboard.press_and_release('e')
        sleep(0.5)
        mouse.click(button='left')
        sleep(0.3)
        keyboard.press('space')
        sleep(3)
        keyboard.release('space')

def combo_s(quantidade):
    for c in range(0, quantidade + 1):
        mouse.click(button='left')
        sleep(0.3)


keyboard.add_hotkey('p', defesa)
keyboard.add_hotkey('o', lambda:esquiva(2))
keyboard.add_hotkey('i', lambda:pulo(2))
keyboard.add_hotkey('3', lambda:combo_1(2))
keyboard.add_hotkey('4', lambda:combo_2(2))
keyboard.add_hotkey('5', lambda:combo_super(2))
keyboard.add_hotkey('x', lambda:combo_s(3))


keyboard.wait('esc')