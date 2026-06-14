import tkinter as tk
from tkinter import *
from tkinter import ttk

operations = ["÷", "x", "-", "+", "="]
oder_oper = ["AC", "()", "%", ".", "c"]
root = tk.Tk()

root.geometry("300x275")
root.title("Calculator")
root.resizable(0, 0)
root.configure(bg="gray24")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
text_result.configure(bg="gray24", fg="white", borderwidth=0)
calculations = ""
times = 0


def add_val_calculatuin(value):
    global calculations
    if value == operations[0]:
        calculations += "/"
    elif value == operations[1]:
        calculations += "*"
    elif value == oder_oper[1]:
        global times
        if times == 0:
            calculations += "("
            times += 1
        else:
            calculations += ")"
            times -= 1
    else:
        calculations += str(value)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculations)


def evaluate_calc():
    global calculations
    try:
        calculations = str(eval(calculations))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculations)
    except:
        clear_calculations()
        text_result.insert(1.0, "Error")


def clear_calculations():
    global calculations
    calculations = ""
    text_result.delete(1.0, "end")


def set_gui():

    for i in range(10):
        globals()[f"btn_num_{i}"] = tk.Button(root, text=(f"{i}"), width=5, font=(
            "Arial", 14), bg="gray51", fg="white", command=lambda i=i: add_val_calculatuin(i))
        globals()[f"btn_num_{i}"].grid(row=3 if i == 7 or i == 8 or i == 9 else 5 if i == 1 or i == 2 or i == 3 else 4 if i == 4 or i == 5 or i == 6 else 6,
                                       column=1 if i == 0 or i == 1 or i == 4 or i == 7 else 2 if i == 2 or i == 5 or i == 8 else 3)
    for i in range(5):
        globals()[f"btn_operation_{i}"] = tk.Button(root, text=(operations[i]), width=5, font=(
            "Arial", 14), bg="misty rose" if i == 4 else "LightSlateGrey", fg="white", command=lambda i=i: add_val_calculatuin(operations[i]) if i != 4 else evaluate_calc())
        globals()[f"btn_operation_{i}"].grid(row=(2 + i),
                                             column=4)
    for i in range(5):
        globals()[f"btn_oder_{i}"] = tk.Button(root, text=(oder_oper[i]), width=5, font=(
            "Arial", 14), bg="LightSkyBlue" if i == 0 else "gray51" if i == 3 or i == 4 else "LightSlateGrey", fg="white", command=lambda i=i: add_val_calculatuin(oder_oper[i]) if i == 1 or i == 2 or i == 3 else clear_calculations())
        globals()[f"btn_oder_{i}"].grid(row=2 if i == 0 or i == 1 or i == 2 else 6,
                                        column=2 if i == 1 or i == 3 else 3 if i == 2 or i == 4 else 1)


set_gui()
root.mainloop()
