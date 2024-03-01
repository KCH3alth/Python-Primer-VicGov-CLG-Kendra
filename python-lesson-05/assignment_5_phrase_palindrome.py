phrase = input("Please submit a phrase to check if it is a palindrome: ").lower()

letters_list_no_space = list(phrase.replace(" ",""))
# Above step removes spaces from the phrase and then converts it to a list of letters.
joined_letters = "".join(letters_list_no_space)
letters_list_no_space.reverse()
reversed_phrase = "".join(letters_list_no_space)

if joined_letters == reversed_phrase:
    is_isnt = 'is'
    print_text_if_input_is_not_a_palindrome = ''
else:
    is_isnt = 'is not'
    print_text_if_input_is_not_a_palindrome = (f" '{phrase.capitalize()}' backwards is '{reversed_phrase}'")
# Added .capitalize() to this string so that the sentence is properly formatted - the phrase had been converted to lowercase at the input stage so the functions and methods could be performed accurately.

print(f"Your suggestion '{phrase}', {is_isnt} a palindrome.{print_text_if_input_is_not_a_palindrome}\n")