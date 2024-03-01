phrase = input("Please submit a phrase to check if it is a palindrome: ").lower()

# Creating variable of all the punctuation elements i want to remove from my string
punctuation = ",.? !'"

# Loop to remove punctuation marks from my phrase
for i in phrase:
    if i in punctuation:
        phrase = phrase.replace(i,"")

letters_list_no_punctuation = list(phrase)
joined_letters = "".join(letters_list_no_punctuation)

letters_list_no_punctuation.reverse()
reversed_phrase = "".join(letters_list_no_punctuation)

if joined_letters == reversed_phrase:
    is_isnt = 'is'
    print_text_if_input_is_not_a_palindrome = ''
else:
    is_isnt = 'is not'
    print_text_if_input_is_not_a_palindrome = (f" '{phrase.capitalize()}' backwards is '{reversed_phrase}'")
# Added .capitalize() to the above string so that the sentence is properly formatted - the phrase had been converted to lowercase at the input stage so the functions and methods could be performed accurately.

print(f"Your suggestion '{phrase}', {is_isnt} a palindrome.{print_text_if_input_is_not_a_palindrome}\n")