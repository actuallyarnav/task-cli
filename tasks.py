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
    new_id = max([task["ID"] for task in tasks_data["tasks"]], default = 0)+1
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
    return 1


def delete_task(task_id):
    return 1


def update_task(task_id, new_task):
    return 1

def mark_task(task_id, status):
    return 1

def clear_tasks():
    with open(TASKS_FILE, "r+") as file:
        file.seek(0)
        json.dump({"tasks": []}, file)
        file.truncate()
