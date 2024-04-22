def palindrome_checker(self):
    user_input = self.entry_0.get()
    phrase = user_input.lower()
    punctuation = ",.? !'-"

    for i in phrase:
        if i in punctuation:
            phrase = phrase.replace(i,"")
    letters_list_no_punctuation = list(phrase)
    joined_letters = "".join(letters_list_no_punctuation)

    letters_list_no_punctuation.reverse()
    reversed_phrase = "".join(letters_list_no_punctuation)

    if joined_letters == reversed_phrase:
        self.label_2['text'] = f"Yes! Your suggestion '{user_input}' is a palindrome."
        self.label_2['bg'] = '#A1C398'
    else:
        self.label_2['text'] = f"No, your suggestion '{user_input}' is not a palindrome.\n\n '{user_input}' backwards is '{reversed_phrase}'"
        self.label_2['bg'] = '#FA7070'
        self.btn_1['text'] = 'Try again'
    return