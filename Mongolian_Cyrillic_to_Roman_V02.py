# Mongolian_Cyrillic_to_Roman_V02
# Mongolians often use Roman Letters for Texting.
# This program converts Cyrillic to Roman letters.
# Some variations exist and you may edit the replacement list accordingly.
# Author: Leo Rauschenberger 2022
#
# 

from transliterate import translit, get_available_language_codes
#import unicodedata
import re

# Test if user actually entered cyrillic
def IsCyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))

# Program Loop
i = 1
while i < 10:
  inputText = input("Enter Text in Cyrillic: ")
  
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
                     'Ө': 'u', 'ө': 'u',  # or o
                     'К': 'K', 'к': 'k',
                     'Л': 'L', 'л': 'l',
                     'М': 'M', 'м': 'm',
                     'Н': 'H', 'н': 'h',
                     'О': 'O', 'о': 'o',
                     'П': 'P', 'п': 'p',
                     'Р': 'R', 'р': 'r',
                     'С': 'S', 'с': 's',
                     'Т': 'T', 'т': 't',
                     'У': 'U', 'у': 'u',
                     'Ү': 'U', 'ү': 'u', # or v
                     'Ф': 'F', 'ф': 'f',
                     'Х': 'H', 'х': 'h', # or X or KH
                     'Ц': 'Ts', 'ц': 'ts',
                     'Ч': 'Ch', 'ч': 'ch',
                     'Ш': 'Sh', 'ш': 'sh',
                     'Ь': 'I', 'ь': 'i',
                     'Ъ': 'I', 'ъ': 'i',
                     'Ы': 'I', 'ы': 'i',
                     'Э': 'E', 'э': 'e',
                     'Ю': 'Yu', 'ю': 'yu',
                     'Я': 'Ya', 'я': 'ya'}
  # Iterate over all key-value pairs in list
  if IsCyrillic(inputText) == 1:
      for key, value in char_to_replace.items():
          outputText = inputText.translate(str.maketrans(char_to_replace))
      print("Conversion result:", outputText)
  else:
      print("Please enter a text in Cyrillic!")
  i += 1


