import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        updated_task = task_entry.get()
        if updated_task:
            tasks[selected_task_index[0]] = updated_task
            update_listbox()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


obj = tk.Tk()
obj.title("To-Do List Application")
obj.config(bg='seashell3')
obj.geometry('330x300')


tasks = []


task_entry = tk.Entry(obj, width=20,font=('calibri',13,'bold'))
task_entry.grid(row=0, column=0, padx=10, pady=10)


add_button = tk.Button(obj, text="Add Task", command=add_task, bg='PeachPuff4')
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_button = tk.Button(obj, text="Remove Task", command=remove_task, bg='ivory4')
remove_button.grid(row=1, column=0, padx=10, pady=10)

update_button = tk.Button(obj, text="Update Task", command=update_task, bg='ivory4')
update_button.grid(row=1, column=1, padx=10, pady=10)


task_listbox = tk.Listbox(obj, width=40, height=10,font=('calibri',10,'bold'))
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


update_listbox()

obj.mainloop()
