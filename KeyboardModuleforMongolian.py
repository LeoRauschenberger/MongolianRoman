# Keyboard module in Python for Mongolian

import keyboard

def barred_o():
    keyboard.send('backspace')
    keyboard.write('ө')

def big_barred_o():
    keyboard.send('backspace')
    keyboard.write('Ө')

def straight_y():
    keyboard.send('backspace')
    keyboard.write('ү')

def big_straight_y():
    keyboard.send('backspace')
    keyboard.write('Ү')

keyboard.add_hotkey('ө', barred_o)
keyboard.add_hotkey('shift+ө', big_barred_o)
keyboard.add_hotkey('ү', straight_y)
keyboard.add_hotkey('shift+ү', big_straight_y)


keyboard.wait('esc')
