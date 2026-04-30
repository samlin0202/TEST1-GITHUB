# main.py

import sys

FILE = "tasks.txt"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return f.read().splitlines()
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        f.write("\n".join(tasks))

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks.pop(index - 1)
        save_tasks(tasks)

# 指令控制
if __name__ == "__main__":
    command = sys.argv[1]

    if command == "list":
        list_tasks()
    elif command == "add":
        add_task(sys.argv[2])
    elif command == "remove":
        remove_task(int(sys.argv[2]))