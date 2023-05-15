"""
Program that takes any String input and converts it into Morse Code
-	Dash (dahs)
.	Dot (dits)
Space	Letter separator
/	Word separator
#	Untranslatable character
"""

from morse_code import *

string_to_convert = input("Your input: ")
output = ""

for element in string_to_convert:
    if element == " ":
        code = "/"
    else:
        try:
            code = morse_code[element.upper()]
        except KeyError:
            code = "#"
    output += code
    output += " "

print(f"In Morse's code:\n{output}")
