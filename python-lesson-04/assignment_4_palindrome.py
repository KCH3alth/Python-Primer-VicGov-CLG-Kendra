# Write some code that will take an input word from a user and check if this word is a palindrome.
word = input("Please submit a word to check if its a palindrome: ")

letters = list(word.lower())
## I added the .lower() because during testing I found the result would always say false if sentence case had been used on the input word.
letters.reverse()
reversed_word = "".join(letters)
palindrome_check = (word.lower() == reversed_word)

print(f"Is {word} a palindrome? {palindrome_check}.\n")

## Alternate sentences to test 'if/else' and make a better sounding answer. 
## If the users input was not a palindrome it will show them what their input looks like when reversed.
if palindrome_check == True:
    is_isnt = 'is'
    not_palindrome = ''
else:
    is_isnt = 'is not'
    not_palindrome = (f" {word} backwards is {reversed_word}")
  
print(f"Your suggestion '{word}', {is_isnt} a palindrome.{not_palindrome}\n")