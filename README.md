# Mongolian to Roman Converter

Mongolians often use Roman letters for texting.</br>
This program converts Cyrillic to Roman letters.</br>
Some variations exist and you may edit the replacement list in the script accordingly. </br>
The script can only convert from Cyrcillic to Roman letters, not the other way around (because that could not be described by a function since "i" can be  И, Й, Ь, Ы or Ъ)</br>
Python IDLE is based on Tkinter and has an unfortunate bug that converts the letters Ү (Cyrillic Straight U) and Ө (Cyrillic Barred O) into a question mark when typed in from the keyboard. You can use an IDE that avoids Tkinter e.g. Spyder. I also found a solution on how to get back those letters in Python.

Standard Replacment list (char_to_replace_1):</br>

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

Replacement list according to Standard MNS 5217: 2012, source: https://estandard.gov.mn/standard/reader/4635

| Cyrillic | Roman |
|:--------:|:-----------:|
| А | A |
| Б | B |
| В | V |
| Г | G |
| Д | D |
| Е | Ye |
| Ё | Yo |
| Ж | J |
| З | Z |
| И | I |
| Й | I | 
| Ө | Ö |
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
| Ү | Ü |
| Ф | F |
| Х | Kh |
| Ц | Ts | 
| Ч | Ch |
| Ш | Sh |
| Ь | I |
| Ъ | I |
| Ы | Y |
| Э | E |
| Ю | Yu | 
|Я | Ya |


Glossika differs again in the following:</br>

| Cyrillic | Roman |
|:--------:|:-----------:|
| Е | Je |
| Ж | Zh |
| Й | J |
| Х | X |
| Ю | Ju |
    
