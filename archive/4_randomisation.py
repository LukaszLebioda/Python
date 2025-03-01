import random

# some random python-in-build functions
# no arguments, 0.0 <= X < 1.0 (0 inclusive, 1 exclusive)
random_float_1 = random.random()
random_float_2 = random.random() * 10
# 2 arguments, a <= X <= b (float, a inclusive, b inclusive)
random_float_3 = random.uniform(1, 10)
# 2 arguments, a <= X <= b (integer, a inclusive, b inclusive)
random_int_4 = random.randint(0, 1)

# game of "Heads or Tails"
random_0_or_1 = round(random.randint(0, 1))
print(random_0_or_1)
if random_0_or_1 == 0:
    print("Heads")
else:
    print("Tails")