# --------------------------------------------------------------
# ctrl + R => to run code
# terminal => python3 (to enter python REPL), quit() (to quit),
# python3 filename.py (to run a file),
# --------------------------------------------------------------

# if, elif, else, nested if, and, or, not
# can You go for a ride in a rollercoaster

height = int(input("How tall are You (cm)? "))
bill = 0

if height > 120:
    print("You're welcome to come in! ")
    age = int(input("How old are You? "))
    if age <= 12:
        bill = 5
        print("Child ticket is 5$ ")
    elif age <= 18:
        bill = 7
        print("Youth ticket is 7$ ")
    elif age >= 45 and age <= 55:
        print("Have a free ride :)")
    else:
        bill = 12
        print("Adult ticket is 12$ ")

    wants_photo = input("Do You want a photo? It's 3$ extra. Type y/n ")
    if wants_photo == "y":
        bill += 3

    print(f"Please pay: {bill}$")
else:
    print("Sorry, You're too short to come in... ")



