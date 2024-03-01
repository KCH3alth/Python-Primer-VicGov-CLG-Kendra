word = input("Please submit a word to check if its a palindrome: ").lower()

letters = list(word)
## I added the .lower() because during testing I found the result would always say false if sentence case had been used on the input word.
letters.reverse()
reversed_word = "".join(letters)
palindrome_check = (word == reversed_word)
print(f"Is {word} a palindrome? {palindrome_check}.\n")

## Alternate sentences to test 'if/else' and make a better sounding answer. 
## If the users input was not a palindrome it will show them what their input looks like when reversed.
if palindrome_check == True:
    is_isnt = 'is'
    text_to_print_if_input_is_not_a_palindrome = ''
else:
    is_isnt = 'is not'
    text_to_print_if_input_is_not_a_palindrome = (f" {word.capitalize()} backwards is {reversed_word}")
  
print(f"Your suggestion '{word}', {is_isnt} a palindrome.{text_to_print_if_input_is_not_a_palindrome}\n")