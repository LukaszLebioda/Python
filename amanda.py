# ----------------------------------------------------
# ctrl + R => to run code
# terminal => python3 (to enter python REPL), quit()
# python3 filename.py (to run a file),
# https://thonny.org/ => debug IDE for python
# ----------------------------------------------------

# For Loops
# Range
# Code Blocks
# Password Generator

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
# add all nubmers from 1 to 100:
sum = 0
for number in range(1, 101):
    sum += number
print(sum)