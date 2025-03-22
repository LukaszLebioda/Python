# # For Loops
# # Ranges
# # FizzBuzz challenge
# # Password Generator

# FOR LOOP to print items from the list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit + "_pie")
    print(fruit + "_juice")

# FOR LOOP to sum items from the list (instead of sum())
# python has in-built sum() function, but we do this on our own
scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 110, 120, 100]
# scores_sum = sum(scores)
# print(scores_sum)
sum = 0
for score in scores:
    sum += score
print(sum)

# FOR LOOP to pick max number of the list (instead of max())
scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 110, 120, 100]
# scores_max =max(scores)
# print(scores_max)
max = 0
for score in scores:
    if score > max:
        max = score
print(max)
    
# FOR LOOP with range()
for number in range(1, 11):
    print(number)

# FOR LOOP with range()
# additional parameter: step
for number in range(1, 11, 2):
    print(number)

# FOR LOOP with range()
# add all numbers from 1 to 100:
sum = 0
for number in range(1, 101):
    sum += number
print(sum)

# FizzBuzz Challenge
for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_list = []

for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
print("Phase 1:", password_list)

for number in range(0, nr_numbers):
    password_list += random.choice(numbers)
print("Phase 2:", password_list)

for symbol in range(0, nr_symbols):
    password_list += random.choice(symbols)
print("Phase 3:", password_list)

random.shuffle(password_list)
print("Phase 4 - shuffled:", password_list)

password = ""
for element in password_list:
    password += element
print("Phase 5 - final password", password)