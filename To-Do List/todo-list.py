import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"title": task, "done": False})
        entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Empty Task", "Task cannot be empty!")

def toggle_done(index):
    tasks[index]["done"] = not tasks[index]["done"]
    refresh_tasks()

def delete_task(index):
    del tasks[index]
    refresh_tasks()

def refresh_tasks():
    for widget in frame_tasks.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        task_frame = tk.Frame(frame_tasks)
        task_frame.pack(fill="x", pady=2)

        task_text = task["title"]
        if task["done"]:
            task_label = tk.Label(task_frame, text=task_text, fg="gray", font=("Arial", 12, "overstrike"))
        else:
            task_label = tk.Label(task_frame, text=task_text, font=("Arial", 12))

        task_label.pack(side="left", padx=5)
        done_button = tk.Button(task_frame, text="✓", width=3, command=lambda i=index: toggle_done(i))
        done_button.pack(side="right", padx=2)
        del_button = tk.Button(task_frame, text="🗑", width=3, command=lambda i=index: delete_task(i))
        del_button.pack(side="right")

# Setup UI
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.resizable(False, False)

title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"))
title.pack(pady=10)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, width=25, font=("Arial", 14))
entry.pack(side="left", padx=10)

add_btn = tk.Button(entry_frame, text="Add Task", command=add_task)
add_btn.pack(side="right")

# Scrollable task area
task_canvas = tk.Canvas(root)
frame_tasks = tk.Frame(task_canvas)
scrollbar = tk.Scrollbar(root, orient="vertical", command=task_canvas.yview)
task_canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
task_canvas.pack(side="left", fill="both", expand=True)
task_canvas.create_window((0, 0), window=frame_tasks, anchor='nw')

def on_frame_configure(event):
    task_canvas.configure(scrollregion=task_canvas.bbox("all"))

frame_tasks.bind("<Configure>", on_frame_configure)

refresh_tasks()
root.mainloop()
