def vowel_counting():
    user_input = self.entry_0.get()
    vowels = "aeiouAEIOU"
    count = 0
    for letter in user_input:
        if letter in vowels:
            count = count +1
    if count == 1:
        self.label_4['text'] = f'\nThere is {count} vowel in your suggestion.\n'
    else:
        self.label_4['text'] = f'\nThere are {count} vowels in your suggestion.\n'
    return