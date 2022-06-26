# Mongolian to Roman Converter

Mongolians often use Roman letters for texting.</br>
This program converts Cyrillic to Roman letters.</br>
Some variations exist and you may edit the replacement list in the script accordingly. </br>
The script can only convert from Cyrcillic to Roman letters, not the other way around (because that could not be described by a function since "i" can be  И, Й, Ь, Ы or Ъ)</br>
Python IDLE is based on Tkinter and has an unfortunate bug that converts the letters Ү (Cyrillic Straight U) and Ө (Cyrillic Barred O) into a question mark when typed in from the keyboard. You can use the AHK script (you need AHK: https://www.autohotkey.com) to fix that issue or use an IDE that avoids Tkinter e.g. Spyder.
Edit: I found a solution on how to get back those letters in Python (see script KeyboardModuleforMongolian.py)

Standart Replacment list:</br>

| Cyrillic | Roman |
|:--------:|:-----------:|
| А | A |
| Б | B |
| В | V |
| Г | G |
| Д | D |
| Е | E |
| Ё | Yo |
| Ж | J |
| З | Z |
| И | I |
| Й | I | 
| Ө | U |
| К | K |
| Л | L |
| М |  M |
| Н | N |
| О | O |
| П | P |
| Р | R |
| С | S |
| Т | T |
| У | U |
| Ү | U |
| Ф | F |
| Х | H |
| Ц | Ts | 
| Ч | Ch |
| Ш | Sh |
| Ь | I |
| Ъ | I |
| Ы | I |
| Э | E |
| Ю | Yu | 
|Я | Ya |


Glossika differs again in the following:</br>

| Cyrillic | Roman |
|:--------:|:-----------:|
| Й | J |
| Х | X |
| Ю | Ju |
    
