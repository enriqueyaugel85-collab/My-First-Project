import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import json
root = tk.Tk()

root.geometry("800x500")
root.title("To do list")
root.resizable(0, 0)
root.configure(bg="gray24")


btns = []
labels = []
have_task = False

try:
    with open("task.json", "r") as file:
        task = json.load(file)
        have_task = True
except FileNotFoundError:
    task = []


def set_task_gui():
    global task_entry
    global btn_check
    task_entry.grid(column=3, row=2)
    btn_check.grid(column=4, row=2)


def add_task(add):
    global task_entry
    global task
    global btn_check
    global labels
    global btns
    if add:
        task += [task_entry.get()]

    num_task = len(task) - 1

    globals()[f"label_task{num_task}"] = tk.Label(root, text=(f"{task[num_task]}"), font=(
        "Arial", 14))

    labels.append([f"label_task{num_task}"])
    globals()[f"btn_box{num_task}"] = tk.Button(root, text="☐", width=6, height=3, font=(
        "Arial", 14), command=lambda num=num_task: delete_task(num), bg="blue", fg="white")
    btns.append([f"btn_box{num_task}"])

    btn_check.grid_remove()
    task_entry.grid_remove()

    row_pos = 3 + num_task
    globals()[f"label_task{num_task}"].grid(column=3, row=row_pos)
    globals()[f"btn_box{num_task}"].grid(column=2, row=row_pos)
    with open("task.json", "w") as file:
        json.dump(task, file, indent=4)


def delete_task(num):
    print("Deleting button")
    task.remove(globals()[f"label_task{num}"]["text"])
    with open("task.json", "w") as file:
        json.dump(task, file, indent=4)
    globals()[f"btn_box{num}"].destroy()
    globals()[f"label_task{num}"].destroy()


btn_add = tk.Button(root, text="+", width=6, height=3, font=(
    "Arial", 14), command=lambda: set_task_gui(), bg="blue", fg="white")
btn_add.grid(column=2, row=2)
btn_check = tk.Button(root, text="✓", width=6, height=3, font=(
    "Arial", 14), command=lambda: add_task(True), bg="blue", fg="white")
task_entry = tk.Entry(root, font=("Arial", 14), width=20)
if have_task:
    add_task(False)

root.mainloop()
