import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label_1 = tk.Label(self, text="Please submit a phrase to check if it is a palindrome: ", 
            fg='#000000', bg='#B3C8CF')
        self.label_1.pack()
        self.entry_0 = tk.Entry(self, bg='#ddf3f5')
        self.entry_0.pack()
        self.label_2 = tk.Label(self, fg='#3C3633', bg='#EADBC8')
        self.label_2.pack()
        self.btn_1 = tk.Button(self, text='Submit', command=self.palindrome_checker)
        self.btn_1.pack()
        
        self.label_3 = tk.Label(self, text="Would you like to know how many vowels are in your suggested palindrome?", 
            fg='#000000', bg='#B3C8CF')
        self.label_3.pack()
        self.btn_2 = tk.Button(self, text='Yes please!', command=self.vowel_counting)
        self.btn_2.pack()
        self.label_4 = tk.Label(self, fg='#3C3633', bg='#EADBC8')
        self.label_4.pack()
 
    def palindrome_checker(self):
        phrase = self.entry_0.get().lower()
        user_input = self.entry_0.get()
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
    
    def vowel_counting(self):
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
    
if __name__ == '__main__':
    root = Root()
    root.title('Palindrome Detector')
    root['bg'] = '#EADBC8'
    root.mainloop()