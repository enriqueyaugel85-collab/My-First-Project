import random
import string
import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
user_options = ["Yes", "No", "Submit"]

questions = ["Enter desired password length: ",
             "Include uppercase letters?", "Include special letters?", "Include digits?", "What app you want it for?", "Do you want to save the pasword?"]
ques_num = 0
password_leng = 0
letters = ""
letter_upper = ""
special = ""
digits = ""
app = ""


def create_password(current_question, user_ans):
    gen_password = ""
    global password_leng
    global letters
    global letter_upper
    global special
    global digits
    letters = string.ascii_lowercase
    if current_question == 0:
        password_leng = user_ans if user_ans else 12
    if current_question == 1:
        letter_upper = string.ascii_uppercase if user_ans == "yes" else ""
    elif current_question == 2:
        special = string.punctuation if user_ans == "yes" else ""
    elif current_question == 3:
        digits = string.digits if user_ans == "yes" else ""
    elif current_question == 4:
        app = user_ans if user_ans else "unkwon"

    elif current_question == 5:

        char = letters + letter_upper + special + digits
        for i in range(password_leng):
            gen_password += random.choice(char)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, gen_password)
    if current_question <= 4:
        global ques_num
        ques_num = current_question + 1
        set_password_gui()
        text_result.delete(1.0, "end")
        text_result.insert(1.0, questions[ques_num])


def submit():
    global entry_answer
    global ques_num
    global btn_sub
    if ques_num == 0:
        try:
            answer = int(entry_answer.get())
            if answer > 8 and answer < 30:
                text_result.delete(1.0, "end")
                create_password(ques_num, answer)
                set_password_gui()
                btn_sub.grid_remove()
                entry_answer.grid_remove()

        except (ValueError):
            pass
    elif ques_num == 4:
        text_result.delete(1.0, "end")
        answer = str(entry_answer.get())
        create_password(ques_num, answer)
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
    if ques_num == 0:
        text_result.insert(1.0, questions[ques_num])
    if ques_num == 1:

        btn_yes.grid(row=2, column=2)

        btn_no.grid(row=3, column=2)
    if ques_num == 4:
        btn_yes.grid_remove()
        btn_no.grid_remove()
        btn_sub.grid(row=3, column=0)
        entry_answer.grid(row=2, column=0)
    if ques_num == 5:
        btn_yes.grid(row=2, column=2)
        btn_no.grid(row=3, column=2)


btn_yes = tk.Button(root, text=(user_options[0]), width=15, font=(
    "Arial", 14), command=lambda: create_password(ques_num, "yes"))
btn_no = tk.Button(root, text=(user_options[1]), width=15, font=(
    "Arial", 14), command=lambda: create_password(ques_num, "no"))
btn_sub = tk.Button(root, text=(user_options[2]), width=15, font=(
    "Arial", 14), command=lambda: submit())
text_result = tk.Text(root, height=5, width=34, font=("Arial", 24))
text_result.grid(columnspan=5)
text_result.configure(bg="gray34", fg="white", borderwidth=0)
btn_sub.grid(row=3, column=0)
entry_answer = tk.Entry(root, font=("Arial", 14))
entry_answer.grid(row=2, column=0)
root.geometry("600x300")
root.title("Calculator")
root.resizable(0, 0)
root.configure(bg="gray24")
set_password_gui()
root.mainloop()

# while True:
# password = create_password()
# print(f"These is your final password: {password}")
# ask_user = input("You want to create another password? (y/n)")
# if ask_user.lower() == "n":
#    break
