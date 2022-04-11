# Mongolian to Roman Converter

Mongolian Cyrillic to Roman Converter</br>
Mongolians often use Roman Letters for Texting.</br>
This program converts Cyrillic to Roman letters.</br>
Some variations exist and you may edit the replacement list in the script accordingly. </br>
The script can only convert from Cyrcillic to Roman letters, not the other way around (because that could not be described by a function since "i" can be  И, Й, Ь, Ы or Ъ)</br>
Python IDLE is based on Tkinter and has an unfortunate bug that converts the letters Ү (Cyrillic Straight U) and Ө (Cyrillic Barred O) into ? when typed in from the keyboard. You can use the AHK script (you need AHK: https://www.autohotkey.com) to fix that issue or use an IDE that avoids Tkinter e.g. Spyder.

Replacment list:</br>
'А'-> 'A', 'а'-> 'a'</br>
'Б'-> 'B', 'б'-> 'b'</br>
'В'-> 'V', 'в'-> 'v'</br>
'Г'-> 'G', 'г'-> 'g'</br>
'Д'-> 'D', 'д'-> 'd'</br>
'Е'-> 'E', 'е'-> 'e'</br>
'Ё'-> 'Yo','ё'-> 'yo'</br>
'Ж'-> 'J', 'ж'-> 'j'</br>
'З'-> 'Z', 'з'-> 'z'</br>
'И'-> 'I', 'и' -> 'i'</br>
'Й'-> 'I' , 'й'-> 'i' or J/j</br>
'Ө'-> 'u', 'ө'-> 'u' or O/o</br>
'К'-> 'K', 'к'-> 'k'</br>
'Л'-> 'L', 'л'-> 'l'</br>
'М'-> 'M', 'м'-> 'm'</br>
'Н'-> 'n', 'н'-> 'n'</br>
'О'-> 'O', 'о'-> 'o'</br>
'П'-> 'P', 'п'-> 'p'</br>
'Р'-> 'R', 'р'-> 'r'</br>
'С'-> 'S', 'с'-> 's'</br>
'Т'-> 'T', 'т'-> 't'</br>
'У'-> 'U', 'у'-> 'u'</br>
'Ү'-> 'U', 'ү'-> 'u' or V/v</br>
'Ф'-> 'F', 'ф'-> 'f'</br>
'Х'-> 'H', 'х'-> 'h' or X/h or KH/kh</br>
'Ц'-> 'Ts', 'ц'-> 'ts'</br>
'Ч': 'Ch', 'ч'-> 'ch'</br>
'Ш'-> 'Sh', 'ш'-> 'sh'</br>
'Ь'-> 'I', 'ь'-> 'i'</br>
'Ъ'-> 'I', 'ъ'-> 'i'</br>
'Ы'-> 'I', 'ы'-> 'i'</br>
'Э'-> 'E', 'э'-> 'e'</br>
'Ю'-> 'Yu', 'ю'-> 'yu'</br>
'Я'-> 'Ya', 'я' -> 'ya'</br>

