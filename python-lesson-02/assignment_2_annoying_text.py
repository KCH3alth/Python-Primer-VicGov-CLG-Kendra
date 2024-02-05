# Create variable original text and assign a string value to it
original_text = "I'm still learning! "
# Create a variable shouting_text. Turn your original_text into upper case and assign the value to the new variable.
shouting_text = original_text.upper()
# Create a variable annoying_text. Repeat your shouting_text 10 times and assign the value to the new  variable.
annoying_text = (10 * shouting_text)
# Use F-strings to write two reports: 
print(f"My annoying text is {annoying_text}")
print(f"My annoying text has {len(annoying_text)} characters.")
# I added an extra report line to get the length of my original text.
print(f"My original text had {len(original_text)} characters.")

# While doing this assignment i kept getting [TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'] issues and errors with my len function. 
# I eventually realised that this was because I was trying to multiply variables that contained a print function.
# E.g. i had shouting_text = print(original_text.upper()) -> so then annoying_text was giving me that error. 
# Removing the print functions from the variable creation steps fixed all my issues.