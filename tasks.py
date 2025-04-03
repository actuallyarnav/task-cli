import json
import time
#defining constants
TASKS_FILE = "tasks.json"

#functions to load data fom json file and to save data to json file
def load_tasks():
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_task(data):
    with open(TASKS_FILE, "w") as file:
        json.dump(data, file, indent=4)

#list operations
def add_task(task):
    tasks_data = load_tasks()
    new_id = max([task["ID"] for task in tasks_data["tasks"]], default = 1)+1
    timestamp = time.strftime("%d-%m-%YT%H:%M:%SZ", time.localtime())

    new_task = {
        "ID": new_id,
        "description": task,
        "status": "todo",
        "createdAt": timestamp,
        "updatedAt": timestamp
    }
    tasks_data["tasks"].append(new_task)
    save_task(tasks_data)
    return new_id

def list_tasks(todo=False, done=False, in_progress=False):
    tasks_data = load_tasks()
    filtered_tasks = tasks_data["tasks"]
    t_status = "all"
    if todo:
        filtered_tasks = [task for task in filtered_tasks if task["status"] == "todo"]
        t_status = "todo"

    if in_progress:
        filtered_tasks = [task for task in filtered_tasks if task["status"] == "in_progress"]
        t_status = "in-progress"

    if done:
        filtered_tasks = [task for task in filtered_tasks if task["status"] == "done"]
        t_status = "done"

    if not filtered_tasks:
        print("No tasks found")
    else:
        print("Listing",t_status, "tasks:")
        for task in filtered_tasks:
            print(f"[{task['ID']}] {task['description']} - {task['status']}")


def delete_task(task_id):
    return 1


def update_task(task_id, new_task):
    tasks_data = load_tasks()
    for task in tasks_data["tasks"]:
        if (int(task_id) == task["ID"]):
            task["task"] = new_task
            timestamp = time.strftime("%d-%m-%YT%H:%M:%SZ", time.localtime())
            task["updatedAt"] = timestamp
            save_task(tasks_data)
            return

def mark_task(task_id, status):
    tasks_data = load_tasks()
    for task in tasks_data["tasks"]:
        if (int(task_id) == task["ID"]):
            task["status"] = status
            timestamp = time.strftime("%d-%m-%YT%H:%M:%SZ", time.localtime())
            task["updatedAt"] = timestamp
            save_task(tasks_data)
            return

def clear_tasks():
    with open(TASKS_FILE, "r+") as file:
        file.seek(0)
        json.dump({"tasks": []}, file)
        file.truncate()
