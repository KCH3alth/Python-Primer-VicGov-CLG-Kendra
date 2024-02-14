#Notes for coding along with the lesson and assignment
print("I'm happy to learn Python")

#Testing steps before my assignment
#Create variable original text and assign a string value to it
original_text = "This is a test. "
print(original_text)
#Create a variable shouting_text. Turn your original_text into upper case and assign the value to the new variable.
shouting_text = original_text.upper()
print(shouting_text)
#Create a variable annoying_text. Repeat your shouting_text 10 times and assign the value to the new variable - i only repeated 3 times during my test
annoying_text = (3 * shouting_text)
print(annoying_text)
#testing len function
text_length = len(annoying_text)
print(text_length)
#Use F-strings to write two reports: 
print(f"My annoying text is {annoying_text}")
print(f"My annoying text has {len(annoying_text)} characters.")
#I added an extra report line to see the length of my original text.
print(f"My original text had {len(original_text)} characters.")