
import random

while True:
    user_input = input("Roll the dice? (y/n): ")
    if user_input.lower() == "y":
        num_random = random.randint(1, 6)
        num_random2 = random.randint(1, 6)
        random_nums = (num_random, num_random2)
        print(random_nums)
    elif user_input.lower() == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid choice!")
