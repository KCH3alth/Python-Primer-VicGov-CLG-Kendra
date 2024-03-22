def vowel_counting():
    phrase = input("Please submit your name to count how many vowels it has: ")

# Included vowels I want to count in both upper and lowercase to prevent errors. 
# I could have used a .lower() on the input, but then the output in the f-string would not be as neat. 
    vowels = "aeiouAEIOU"
    count = 0
    for letter in phrase:
        if letter in vowels:
            count = count +1
    print(f'\nYour name is {phrase}.')
    if count == 1:
        print(f'There is {count} vowel in your name.\n')
    else:
        print(f'There are {count} vowels in your name.\n')
    return