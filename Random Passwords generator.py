import random
import string
gen_password = ""

password_leng = 0
questions = ["Enter desired password length: ",
             "Include uppercase letters? (y/n): ", "Include special letters? (y/n): ", "Include digits? (y/n): "]


def setting_password(desire_question):
    if desire_question == "letters_upper":
        return string.ascii_uppercase if input(questions[1]).lower() == "y" else ""
    elif desire_question == "special_char":
        return string.punctuation if input(questions[2]).lower() == "y" else ""
    elif desire_question == "digits":
        return string.digits if input(questions[3]).lower() == "y" else ""


def create_password():
    try:
        password_leng = input(questions[0])
    except (ValueError, TypeError):
        print("You dint enter valid number setting length to 12")
        password_leng = 12
        letters = string.ascii_lowercase

    while len(gen_password) != password_leng:

        gen_password += random.choice(letters)
        gen_password += random.choice(setting_password("letters_upper"))
        gen_password += random.choice(setting_password("digits"))
        gen_password += random.choice(setting_password("special_char"))

    print(f"These is your final password: {gen_password}")


while True:
    setting_password("letters_upper")
    ask_user = input("You want to create another password? (y/n)")
    if ask_user.lower() == "n":
        break
