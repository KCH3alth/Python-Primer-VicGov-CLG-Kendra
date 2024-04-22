import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.palindrome_label = tk.Label(self, text="Please submit a phrase to check if it is a palindrome: ", 
            fg="#000000", bg="#B3C8CF", bd="7", font=("Calibri",11))
        self.palindrome_label.pack()
        self.entry = tk.Entry(self, bg="#ddf3f5")
        self.entry.pack()
        self.palindrome_result = tk.Label(self, fg="#3C3633", bg="#EADBC8", font=("Calibri",11))
        self.palindrome_result.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.palindrome_checker)
        self.submit_button.pack()
        
        self.vowel_label = tk.Label(self, text="Would you like to know how many vowels are in your suggested palindrome?", 
            fg="#000000", bg="#B3C8CF", bd="7", font=("Calibri",11))
        self.vowel_label.pack()
        self.vowel_button = tk.Button(self, text="Yes please!", command=self.vowel_counting)
        self.vowel_button.pack()
        self.vowel_result = tk.Label(self, fg="#3C3633", bg="#EADBC8", font=("Calibri",11))
        self.vowel_result.pack()

        self.clear_button = tk.Button(self, text="Click here to clear the entry box", command=self.clear_entry)
        self.clear_button.pack()
 
    def palindrome_checker(self):
        user_input = self.entry.get()
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
            self.palindrome_result["text"] = f"Yes! Your suggestion '{user_input}' is a palindrome."
            self.palindrome_result["bg"] = "#A1C398"
        else:
            self.palindrome_result["text"] = f"No, your suggestion '{user_input}' is not a palindrome.\n\n '{user_input}' backwards is '{reversed_phrase}'"
            self.palindrome_result["bg"] = "#FA7070"
    
    def vowel_counting(self):
        user_input = self.entry.get()
        vowels = "aeiouAEIOU"
        count = 0
        for letter in user_input:
            if letter in vowels:
                count = count +1
        if count == 1:
            self.vowel_result["text"] = f"\nThere is {count} vowel in your suggestion.\n"
        else:
            self.vowel_result["text"] = f"\nThere are {count} vowels in your suggestion.\n"
    
    def clear_entry(self):
        self.entry.delete(0,"end")
    
if __name__ == "__main__":
    root = Root()
    root.title("Palindrome Detector")
    root["bg"] = "#EADBC8"
    root.mainloop()