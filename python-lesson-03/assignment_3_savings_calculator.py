# Initialise three variables: money_start, saving_years, interest_rate
# Assign the values to the three variables using the input() function. Pass an instructional message (string) as an argument to the input function.
money_start = float(input("Please enter the starting balance of your savings account: $"))
saving_years = int(input("How many years will you be saving for? "))
interest_rate = float(input("What is the interest rate on this savings account? ").replace("%",""))
    ## I used str.replace to remove any % symbols that users may accidentally input. When testing this script I kept inadvertantly inputting the interest rate as 4.5% instead of 4.5.
    ## The extra % symbol could potentially cause issues in the later steps, so the replace function above cleaned that up
    ## I then added some print steps to check if my inputs worked (they did, so I removed those print steps from the final code)

# Convert each input to a float or integer, depending on the type of input you are requesting.
    ## I added the conversion step to the start of each input function so it would be cleaner than creating an additional variable for each.
    ## Added print step to check my work on converting types
print()
    ## Added blank print function to insert a blank line in the terminal to make my output clearer
print(f"Variable money_start has {type(money_start)}")
print(f"Variable saving_years has {type(saving_years)}")
print(f"Variable interest_rate has {type(interest_rate)}\n")
    ## Added \n to insert a new line, keeping this print step seperate from the formatted string below.

# Create a variable money_result
# Assign the formula money_start * interest_rate * saving_years to money_result
money_result = money_start * interest_rate * saving_years

# Print money_result to the console in a formatted string.
    ## I added :.2f to the string to format the numbers down to 2 decimal places.
print(f"Total savings would be ${money_result:.2f}, after {saving_years} years in an account with an interest rate of {interest_rate}%.")
    ## Bonus sentence experimenting with math inside of a printed formatted string.
print(f"This is an increase of ${(money_result - money_start):.2f} from the starting balance of ${money_start}\n")

# Is the result more than 10000? If yes, include in your code to print True to the console, otherwise print False.
print(f"True or False? The total balance is more than $10,000. {money_result > 10000}.")
print()