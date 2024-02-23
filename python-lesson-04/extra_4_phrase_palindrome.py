# Version to check if a phrase is a palindrome
phrase = input("Please submit a phrase to check if it is a palindrome: ")

phrase_letters = list(phrase.lower())
phrase_letters.remove(' ')
print(phrase_letters)
phrase_no_space = "".join(phrase_letters)
phrase_letters.reverse()
print(phrase_letters)
reversed_phrase = "".join(phrase_letters)
print(reversed_phrase)

palindrome_check = (phrase_no_space == reversed_phrase.lower())
print(palindrome_check)
if palindrome_check == True:
    is_isnt = 'is'
    not_palindrome = ''
else:
    is_isnt = 'is not'
    not_palindrome = (f" '{phrase}' backwards is '{reversed_phrase}'")
  
print(f"Your suggestion '{phrase}', {is_isnt} a palindrome.{not_palindrome}\n")
#Works for two word phrases, still need to work out how to remove multiple spaces - e.g for a 5 word phrase