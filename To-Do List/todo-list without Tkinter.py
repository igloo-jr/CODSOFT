import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks found.")
        return
    print("\n📝 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task['done'] else "✖"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("✅ Task added.")
    else:
        print("⚠️  Task cannot be empty.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]['done'] = True
            save_tasks(tasks)
            print("✅ Task marked as done.")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Enter task number to delete: ")) - 1
        if 0 <= i < len(tasks):
            deleted = tasks.pop(i)
            save_tasks(tasks)
            print(f"🗑 Deleted: {deleted['title']}")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n====== TO-DO MENU ======")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
