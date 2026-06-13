import random
# Has to have a continue option
# Need to decide a random value out of the options
# needs to be organized
# needs to show who wins and who lost

choices = ["r", "p", "s"]
definitions_choiches = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}


def choice_definitiion(choice):
    if definitions_choiches[choice]:
        return definitions_choiches[choice]
    else:
        print("Invalid answer")


def msg_choices(user_ans, comp_choice):
    try:
        user = choice_definitiion(user_ans)
        comp = choice_definitiion(comp_choice)
        print(f"You choose {user}")
        print(f"He choose {comp}")
    except (KeyError):
        print("Invalid answer")


def continue_opt():
    user_ans = input("You want to continue? (y/n)")
    if user_ans.lower() == "n":
        return False


def choose_winner(user, comp):
    if (user == "r" and comp == "s" or user == "p" and comp == "r" or
            user == "s" and comp == "p"):
        msg_choices(user, comp)
        print("Congratulations")
        print("You win")

    elif user == "r" or "s" or "p":
        msg_choices(user, comp)
        print("You lost")
    elif user == comp:

        msg_choices(user, comp)
        print("Its a tie")


while True:
    user_answer = input("Rock, Paper, Scissors (r/p/s): ")
    comp_choices = random.choice(choices)
    choose_winner(user_answer.lower(), comp_choices)
    conti = continue_opt()
    if conti == False:
        break
    else:
        continue
