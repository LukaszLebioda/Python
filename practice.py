# basic built-in functions:
# print() => prints the output
# len() => returns the length, e.g. of string
# type() => returns the datatype of a variable
# int(), float(), str(), bool() => converts one datatype into another
# round() => rounds floats (with optional precision parameter)
text = "Hello_world"
num = "123"
numConverted = int(num)
numRounded = round(numConverted / 5, 2)
textLength = len(text)
textType = type(text)
print(text, textLength, textType)
print(f"The text is: {text},\nand the number is: {num}.") # f-string
print(numConverted)
print(numRounded)






