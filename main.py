import sys
import os

FILE = "tasks.txt"


# 讀取任務
def load_tasks():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return f.read().splitlines()


# 存回任務
def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))


# 顯示任務
def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("目前沒有任務")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


# 新增任務
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"已新增：{task}")


# 刪除任務（已修正 index bug）
def remove_task(index):
    tasks = load_tasks()

    if index <= 0 or index > len(tasks):
        print("刪除失敗：沒有這個編號")
        return

    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"已刪除：{removed}")

# 全部刪除任務
def clear_tasks():
    save_tasks([])
    print("已清空所有任務")
# 主程式
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("請輸入指令：list / add / remove")
        sys.exit()

    command = sys.argv[1]

    if command == "list":
        list_tasks()

    elif command == "add":
        if len(sys.argv) < 3:
            print("請輸入要新增的任務")
        else:
            add_task(sys.argv[2])

    elif command == "remove":
        if len(sys.argv) < 3:
            print("請輸入要刪除的編號")
        else:
            try:
                remove_task(int(sys.argv[2]))
            except ValueError:
                print("請輸入數字")
    elif command == "clear":
        clear_tasks()
    else:
        print("未知指令：list / add / remove")