# print() => prints the output
# len() => returns the length, e.g. of string
# type() => returns the datatype of a variable
# int(), float(), str(), bool() => converts one datatype into another
# round() => rounds floats (with optional precision parameter)
# input() => asks user for input, can be stored in a variable
# lower(), upper() => lowercase, uppercase

# f-strings

text = "Hello_world"
text_converted = text.lower() # or .upper()
num = "123"
numConverted = int(num)
numRounded = round(numConverted / 5, 2)
textLength = len(text)
textType = type(text)
print(text, text_converted, textLength, textType)
print(f"The text is: {text},\nand the number is: {num}.") # f-string
print(numConverted)
print(numRounded)
someVariable = input("Type anything")
print(someVariable)

# tip calculator
print("Welcome to the tip calculator:")
bill = float(input("What was the total bill? $"))
tipPercentage = int(input("How much tip would you like to give? %"))
numberOfPeople = int(input("How many people are splitting the bill? "))

tipAmount = bill * (tipPercentage / 100)
totalBill = bill + tipAmount
result = round(totalBill / numberOfPeople, 2)

print(f"Each person should pay: {result}")






