# -*- coding: utf-8 -*-
# Mongolian_Cyrillic_to_Roman_V02
# Mongolians often use Roman Letters for Texting.
# This program converts Cyrillic to Roman letters.
# N.B.: The letters Ү (Cyrillic Straight U) and Ө (Cyrillic Barred O) of the Mongolian alphabet can be copied,
# but not typed into Python IDLE due to an unfortunate bug.
# Some variations exist and you may edit the replacement list accordingly.
# Author: Leo Rauschenberger 2022

import re
import sys
import time
import ctypes
import keyboard

# -------------------------------------------------------------
# Replacement List.
char_to_replace = {'А': 'A', 'а': 'a',
                   'Б': 'B', 'б': 'b',
                   'В': 'V', 'в': 'v',
                   'Г': 'G', 'г': 'g',
                   'Д': 'D', 'д': 'd',
                   'Е': 'E', 'е': 'e',
                   'Ё': 'Yo','ё': 'yo',
                   'Ж': 'J', 'ж': 'j',
                   'З': 'Z', 'з': 'z',
                   'И': 'I', 'и': 'i',
                   'Й': 'I', 'й': 'i',  # or j
                   'Ө': 'U', 'ө': 'u',  # or o
                   'К': 'K', 'к': 'k',
                   'Л': 'L', 'л': 'l',
                   'М': 'M', 'м': 'm',
                   'Н': 'N', 'н': 'n',
                   'О': 'O', 'о': 'o',
                   'П': 'P', 'п': 'p',
                   'Р': 'R', 'р': 'r',
                   'С': 'S', 'с': 's',
                   'Т': 'T', 'т': 't',
                   'У': 'U', 'у': 'u',
                   'Ү': 'U', 'ү': 'u', # or v
                   'Ф': 'F', 'ф': 'f',
                   'Х': 'H', 'х': 'h', # or X or Kh
                   'Ц': 'Ts', 'ц': 'ts',
                   'Ч': 'Ch', 'ч': 'ch',
                   'Ш': 'Sh', 'ш': 'sh',
                   'Щ': 'Sh', 'щ': 'sh',
                   'Ь': 'I', 'ь': 'i',
                   'Ъ': 'I', 'ъ': 'i',
                   'Ы': 'I', 'ы': 'i',
                   'Э': 'E', 'э': 'e',
                   'Ю': 'Yu', 'ю': 'yu',
                   'Я': 'Ya', 'я': 'ya'}

# Standart MNS 5217: 2012
# source: https://estandard.gov.mn/standard/reader/4635
char_to_replace_2 = {'А': 'A', 'а': 'a',
                   'Б': 'B', 'б': 'b',
                   'В': 'V', 'в': 'v',
                   'Г': 'G', 'г': 'g',
                   'Д': 'D', 'д': 'd',
                   'Е': 'Ye', 'е': 'ye',
                   'Ё': 'Yo','ё': 'yo',
                   'Ж': 'J', 'ж': 'j',
                   'З': 'Z', 'з': 'z',
                   'И': 'I', 'и': 'i',
                   'Й': 'I', 'й': 'i',
                   'К': 'K', 'к': 'k',
                   'Л': 'L', 'л': 'l',
                   'М': 'M', 'м': 'm',
                   'Н': 'N', 'н': 'n',
                   'О': 'O', 'о': 'o',
                   'Ө': 'Ö', 'ө': 'ö',
                   'П': 'P', 'п': 'p',
                   'Р': 'R', 'р': 'r',
                   'С': 'S', 'с': 's',
                   'Т': 'T', 'т': 't',
                   'У': 'U', 'у': 'u',
                   'Ү': 'Ü', 'ү': 'ü',
                   'Ф': 'F', 'ф': 'f',
                   'Х': 'Kh', 'х': 'kh',
                   'Ц': 'Ts', 'ц': 'ts',
                   'Ч': 'Ch', 'ч': 'ch',
                   'Ш': 'Sh', 'ш': 'sh',
                   'Щ': 'Sh', 'щ': 'sh',
                   'Ь': 'I', 'ь': 'i',
                   'Ъ': 'I', 'ъ': 'i',
                   'Ы': 'Y', 'ы': 'y',
                   'Э': 'E', 'э': 'e',
                   'Ю': 'Yu', 'ю': 'yu',
                   'Я': 'Ya', 'я': 'ya'}

words_to_replace = {'байна': 'bna', 'байна уу': 'bnu', 'сайн': 'sn', 'юм': 'ym', 'зүгээр': 'zgr'}

# Test if user actually entered cyrillic
def IsCyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))

# Perform transliteration
def transliterate(charlist):
    # Iterate over all key-value pairs in list
    for key, value in char_to_replace.items():
        outputText = inputText.translate(str.maketrans(charlist))
    return outputText

# Get language ID as hexadecimal from active window
def сheckLayout():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    handle = user32.GetForegroundWindow()
    threadid = user32.GetWindowThreadProcessId(handle, 0)
    layout_id = user32.GetKeyboardLayout(threadid)
    language_id = hex(layout_id & (2 ** 16 - 1))
    #print(language_id)

    # Applying keyboard fix if Mongolian keyboard is active
    if str(language_id) == "0x450":
        # Debug tkinter such that ? resulting from Ү and Ө entries from the keyboard (equiv. to keyboard.send('...')), the keyboard.write(...) command will be used.
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
        state = "MN"
    else:
        state = "NA"
    return state 

# quit if ESC+Enter is pressed
keyboard.add_hotkey('escape', quit)

# Main Loop ----------------------------------------------------------------
state = ""
state = сheckLayout()
if state == "NA":
    print("Mongolian keyboard input inactive. You can still paste text in.")
elif state == "MN":
    print("Mongolian keyboard layout active. Applying fix for letters Ү and Ө.")


while True:
    time.sleep(.5)
    сheckLayout()
    inputText = input("Enter Text in Cyrillic: ")
    if IsCyrillic(inputText) == 1:
        print("Conversion result-----:", transliterate(char_to_replace_2))
    elif IsCyrillic(inputText) == 0:
        print("Please enter a text in Cyrillic!")
    input("")

keyboard.unhook_all()
