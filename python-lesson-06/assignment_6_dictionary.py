kendra = {
    "age":29,
    "gender":"female",
    "occupation":"Health Scientist",
    "hobby":"playing video games",
    "colour":"blue",
    "degree":"Bachelor of Biomedical Science (Honours)"
}
for value in kendra.values():
    print(('\nKendra is a {age} year old {gender}.').format(**kendra))
    ## Used the above alternate method to streamline a sentence with two variables.
    print(('She works as a {occupation} and in her free time she enjoys {hobby}.').format(**kendra))
    print(f'Her favourite colour is '+ kendra['colour'])
    print(f"Kendra's qualification is a "+ kendra['degree'])
    break

## Updating variables in dictionary
kendra["colour"] = "turquoise"
print(f'\nCorrection. Her favourite colour is '+ kendra["colour"])

print(f'\nYour dictionary is:')
for key, value in kendra.items():
    print(f" - {key}: {value}")

## Removing key and value
kendra.pop("degree")

## Adds key and value
kendra["vegetable"] = "potato"

print(f'\nThe updated dictionary is:')
for key, value in kendra.items():
    print(f" - {key}: {value}")

## Clearing a dictionary
kendra.clear()
print(f'\nThe cleared dictionary is: {kendra}\n')