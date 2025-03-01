# LISTS
fruits = ["cherry", "apple", "berry"]
fruits[-1] = "lemon"
fruits.append("melon")
fruits.extend(["pear", "peach", "mango"])
print(fruits)
print(len(fruits))

# who pays the bill?
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = random.choice(friends)
print(random_friend)

random_index = random.randint(0, len(friends) - 1)
print(friends[random_index])

# NESTED LISTS
fast_food = ["pizza", "burger", "fries"]
healthy_food = ["apple", "banana", "carrot"]
foods = [fast_food, healthy_food]
print(foods)
print(foods[1][0])

# ----------------------------------------------------
# ROCK, PAPER, SCISSORS
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")