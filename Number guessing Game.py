import random
correct_num = random.randint(1, 100)
while True:
    try:
        user_input = int(input("Guess the number between 1 and 100: "))

        if int(user_input) > correct_num:
            print("Too high!")
        elif int(user_input) < correct_num:
            print("Too low!")
        elif int(user_input) == correct_num:
            print("Congratulations you find the number")
            break
    except (ValueError):
        print("Please enter a number")
