# Integer is whole number
# Float is a number with a decimal point eg 10.99 (floating point number)
# Boolean is true/false

# Exponential operator = ** raises one number to the power of another
print(5 ** 3)
# 5 ** 3 = 5 cubed = 5 x 5 x 5 = 125

# Modulo operater = % - returns the remainder when one number is divided by another
print(18 % 7)
# 7 goes into 18 twice with a remainder of 4 so the modulo should = 4
print(20 % 7)

# Floor division operator = // - divides two numbers and gives the nearest integer less than or equal to the result
print(14/3)
print(14//3)
# 14 divided by 3 = 4.67, using floor division provides an answer of 4

c = 4 + 10 / 2
d = (4 + 10) / 2
print(c)
print(d)
print(3>1 and 11 == 11.0)
final_result = (10+3) ** 2 % 3 == 14
print(final_result)

# Converting floats to integers will just remove everything agter the decimal place, will not round the value up if it is .5 or above
# Converting booleans to integers will turn it into binary code

# Inputs come in as strings - need to be converted if you want to use an input number as part of a calculation