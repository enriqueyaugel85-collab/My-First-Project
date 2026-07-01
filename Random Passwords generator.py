import random
import string
import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
root = tk.Tk()
user_options = ["Yes", "No", "Submit"]

questions = ["Enter desired password length: ",
             "Include uppercase letters?", "Include special letters?", "Include digits?", "What app you want it for?"]
ques_num = 0
password_leng = 0
letters = ""
letter_upper = ""
special = ""
digits = ""
app = ""

current_user = None
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except FileNotFoundError, json.JSONDecodeError:
    users = {}
app = ""
initalize_password_set = False


def check_user():
    global users
    global username_entry
    global user_password_entry
    global account
    global initalize_password_set
    global username_label
    global user_password_label
    global btn_sub_user
    global current_user
    password_user = user_password_entry.get()
    user_name = username_entry.get()
    if user_name not in users:
        users[user_name] = {
            "password": password_user,
            "apps": {}
        }
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        current_user = user_name
    elif users[user_name]["password"] == password_user:
        current_user = user_name
    username_entry.grid_remove()
    username_label.grid_remove()
    user_password_entry.grid_remove()
    user_password_label.grid_remove()
    btn_sub_user.grid_remove()
    text_result.grid_remove()
    btn_create_password.grid(row=2, column=2)
    btn_password_lib.grid(row=3, column=2)
    return user_name


def account_setting(user_ans):
    global username_label
    global username_entry
    global user_password_label
    global user_password_entry
    global btn_acc_no
    global btn_acc_yes
    global btn_sub_user
    global initalize_password_set
    global users
    if user_ans == "yes" and len(users) == 0:
        text_result.grid_remove()
        btn_acc_yes.grid_remove()
        btn_acc_no.grid_remove()

        username_label.grid(row=0, column=0)
        username_entry.grid(row=0, column=1)
        user_password_label.grid(row=1, column=0, padx=5, pady=5)
        user_password_entry.grid(row=1, column=1, padx=5, pady=5)
        btn_sub_user.grid(row=2, column=1, padx=5, pady=5)

    elif user_ans == "no":
        initalize_password_set = True
        set_password_gui()


def create_password_handler(current_question, user_ans):
    password = ""
    global password_leng
    global letters
    global letter_upper
    global special
    global digits
    global users
    global app
    global initalize_password_set
    global btn_no
    global btn_yes
    global btn_next
    global current_user
    letters = string.ascii_lowercase
    if current_question == 0:
        password_leng = user_ans if user_ans else 12
        initalize_password_set = True
    elif current_question == 1:
        letter_upper = string.ascii_uppercase if user_ans == "yes" else ""
    elif current_question == 2:
        special = string.punctuation if user_ans == "yes" else ""
    elif current_question == 3:
        digits = string.digits if user_ans == "yes" else ""
    elif current_question == 4:
        app = user_ans if user_ans else "unkwon"
        current_question += 1
        create_password_handler(current_question, user_ans)
    elif current_question == 5 and initalize_password_set == True:
        current_user = check_user()
        char = letters + letter_upper + special + digits
        password = create_password(char)
        text_result.grid(columnspan=5)
        text_result.delete(1.0, "end")
        text_result.insert(
            1.0, [f"For {app} your password is: {password}"])
        btn_no.grid_remove()
        btn_yes.grid_remove()
        btn_next.grid(row=2, column=2)
        btn_del.grid(row=3, column=2)
        initalize_password_set = False
    if user_ans == "save":
        save_password(app, password)
    elif user_ans == "delete":
        delete_password()
    if current_question < 4:
        global ques_num
        ques_num = current_question + 1
        set_password_gui()
        text_result.delete(1.0, "end")
        text_result.insert(1.0, questions[ques_num])


def create_password(char):
    gen_password = ""
    for i in range(password_leng):
        gen_password += random.choice(char)
    return gen_password


def save_password(app, password):
    global users
    global current_user
    global btn_next
    global btn_del
    global text_result
    global btn_create_password
    global btn_password_lib
    btn_next.grid_remove()
    btn_del.grid_remove()
    text_result.grid_remove()
    btn_create_password.grid(row=2, column=2)
    btn_password_lib.grid(row=3, column=2)
    users[current_user]["apps"][app] = password
    with open("users.json", "w") as file:

        json.dump(users, file, indent=4)


def delete_password():
    global btn_next
    global btn_del
    global text_result
    global btn_create_password
    global btn_password_lib
    btn_next.grid_remove()
    btn_del.grid_remove()
    text_result.grid_remove()
    btn_create_password.grid(row=2, column=2)
    btn_password_lib.grid(row=3, column=2)


def submit():
    global entry_answer
    global ques_num
    global btn_sub
    if ques_num == 0:
        try:
            answer = int(entry_answer.get())
            if answer > 8 and answer < 30:
                text_result.delete(1.0, "end")
                create_password_handler(ques_num, answer)
                set_password_gui()
                btn_sub.grid_remove()
                entry_answer.grid_remove()

        except (ValueError):
            pass
    elif ques_num == 4:
        text_result.delete(1.0, "end")
        answer = str(entry_answer.get())
        create_password_handler(ques_num, answer)
        btn_sub.grid_remove()
        entry_answer.grid_remove()


def set_password_gui():
    global questions
    global ques_num
    global password_leng
    global entry_answer
    global btn_sub
    global btn_no
    global btn_yes
    global text_result
    global initalize_password_set
    global user_password_entry
    global user_password_label
    global username_entry
    global username_label
    global btn_sub_user

    if ques_num == 0:

        text_result.grid(columnspan=5)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, questions[ques_num])
        btn_sub.grid(row=3, column=0)
        entry_answer.grid(row=2, column=0)
        initalize_password_set = True
    elif ques_num == 1:

        btn_yes.grid(row=2, column=2)

        btn_no.grid(row=3, column=2)
    elif ques_num == 4:
        btn_yes.grid_remove()
        btn_no.grid_remove()
        btn_sub.grid(row=3, column=0)
        entry_answer.grid(row=2, column=0)
    elif ques_num == 5:
        btn_yes.grid(row=2, column=2)
        btn_no.grid(row=3, column=2)


def set_create_password():
    global ques_num
    global btn_create_password
    global btn_password_lib
    global password_leng
    global letters
    global letter_upper
    global special
    global digits
    global app
    btn_create_password.grid_remove()
    btn_password_lib.grid_remove()
    ques_num = 0
    password_leng = 0
    letters = ""
    letter_upper = ""
    special = ""
    digits = ""
    app = ""
    set_password_gui()


def password_lib_open():
    global current_user
    global btn_create_password
    global btn_password_lib
    global users
    global btn_close
    num = 0

    globals()[f"user_label"] = tk.Label(
        root, text=current_user, font=("Arial", 14))
    keys_list = list(users[current_user]["apps"].keys())
    values_list = list(users[current_user]["apps"].values())

    total_val = len(users[current_user]["apps"])
    globals()[f"user_label"].grid(row=1, column=0)
    btn_create_password.grid_remove()
    btn_password_lib.grid_remove()

    btn_close.grid(row=9, column=5)
    for i in range(total_val):
        app = keys_list[i]
        password = values_list[i]

        globals()[f"label_{app}"] = tk.Label(
            root, text=[f"{app}: "], font=("Arial", 14))

        globals()[f"label_password_{app}"] = tk.Label(
            root, text=[f"{password}"], font=("Arial", 14))

        globals()[f"label_{app}"].grid(row=3 + num, column=0)
        globals()[f"label_password_{app}"].grid(row=3 + num, column=1)

        num += 1


def password_lib_close():
    global current_user
    global btn_create_password
    global btn_password_lib
    global users
    global btn_close
    keys_list = list(users[current_user]["apps"].keys())
    total_val = len(users[current_user]["apps"])
    globals()[f"user_label"].grid_remove()
    btn_close.grid_remove()
    for i in range(total_val):
        app = keys_list[i]
        globals()[f"label_{app}"].destroy()
        globals()[f"label_password_{app}"].destroy()
    btn_create_password.grid(row=2, column=2)
    btn_password_lib.grid(row=3, column=2)


username_entry = tk.Entry(root, font=("Arial", 14))
username_label = tk.Label(root, text=("Username: "), font=(
    "Arial", 14))
user_password_entry = tk.Entry(root, font=("Arial", 14))
user_password_label = tk.Label(root, text=("Pasword: "), font=(
    "Arial", 14))
btn_yes = tk.Button(root, text=(user_options[0]), width=15, font=(
    "Arial", 14), command=lambda: create_password_handler(ques_num, "yes"))
btn_no = tk.Button(root, text=(user_options[1]), width=15, font=(
    "Arial", 14), command=lambda: create_password_handler(ques_num, "no"))
btn_acc_yes = tk.Button(root, text=(user_options[0]), width=15, font=(
    "Arial", 14), command=lambda: account_setting("yes"))
btn_acc_no = tk.Button(root, text=(user_options[1]), width=15, font=(
    "Arial", 14), command=lambda: account_setting("no"))
btn_sub = tk.Button(root, text=(user_options[2]), width=15, font=(
    "Arial", 14), command=lambda: submit())
btn_sub_user = tk.Button(root, text=user_options[2] if len(users) == 0 else "Enter", width=15, font=(
    "Arial", 14), command=lambda: check_user())
btn_password_lib = tk.Button(root, text="Password library", width=15, font=(
    "Arial", 14), command=lambda: password_lib_open())
btn_create_password = tk.Button(root, text="Create password", width=15, font=(
    "Arial", 14), command=lambda: set_create_password())
btn_next = tk.Button(root, text="Save", width=15, font=(
    "Arial", 14), command=lambda: create_password_handler(ques_num, "save"))
btn_del = tk.Button(root, text="Delete", width=15, font=(
    "Arial", 14), command=lambda: create_password_handler(ques_num, "delete"))
btn_close = tk.Button(root, text="Close", width=15, font=(
    "Arial", 14), command=lambda: password_lib_close())
text_result = tk.Text(root, height=5, width=34, font=("Arial", 24))

text_result.configure(bg="gray34", fg="white", borderwidth=0)
text_result.grid(columnspan=5)

entry_answer = tk.Entry(root, font=("Arial", 14))

root.geometry("600x300")
root.title("Password Manager")
root.resizable(0, 0)
root.configure(bg="gray24")
if len(users) == 0:
    text_result.insert(1.0, "Create an account")
    btn_acc_yes.grid(row=2, column=2)
    btn_acc_no.grid(row=3, column=2)
else:
    text_result.insert(1.0, "Sign In")
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1)
    user_password_label.grid(row=2, column=0)
    user_password_entry.grid(row=2, column=1)
    btn_sub_user.grid(row=3, column=1)

root.mainloop()
