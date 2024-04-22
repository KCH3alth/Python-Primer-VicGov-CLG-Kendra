import tkinter as tk
import palindrome_checker as pc
from vowels import vowel_counting
from clear_text import clear_entry

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
        self.btn_1 = tk.Button(self, text='Submit', command=pc.palindrome_checker)
        self.btn_1.pack()
        
        self.label_3 = tk.Label(self, text="Would you like to know how many vowels are in your suggested palindrome?", 
            fg='#000000', bg='#B3C8CF')
        self.label_3.pack()
        self.btn_2 = tk.Button(self, text='Yes please!', command=vowel_counting)
        self.btn_2.pack()
        self.label_4 = tk.Label(self, fg='#3C3633', bg='#EADBC8')
        self.label_4.pack()
 
        self.clear_button = tk.Button(self, text="Click here to clear the entry box", command=self.clear_entry)
        self.clear_button.pack()

if __name__ == '__main__':
    root = Root()
    root.title('Palindrome Detector')
    root['bg'] = '#EADBC8'
    root.mainloop()