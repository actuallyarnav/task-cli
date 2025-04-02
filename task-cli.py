import os
import json
import argparse
from tasks import add_task, delete_task, update_task, mark_task, list_tasks

TASKS_FILE = 'tasks.json'
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump({"tasks": []}, file, indent=4)

def main():
    print("Hi there! This is a task CLI application designed to help you manage your tasks efficiently. Use \"taskcli --help\" to see command usage")
#defining args
parser = argparse.ArgumentParser(description='Task CLI')
subparsers = parser.add_subparsers(dest='command', required=True)

add_parser = subparsers.add_parser('add', help = "add a new task")
add_parser.add_argument('task', help = "description of the task")

list_parser = subparsers.add_parser('list', help = "list tasks (defaults to all tasks)")
list_parser.add_argument('todo', action='store_true', help='list only incomplete tasks')
list_parser.add_argument('done', action='store_true', help='list only completed tasks')
list_parser.add_argument('in-progress', action='store_true', help='list only in-progress tasks')

delete_parser = subparsers.add_parser('delete', help = "delete a task")
delete_parser.add_argument('task_id', type=int, help = "id of the task to delete")

update_parser = subparsers.add_parser('update', help = "update a task")
update_parser.add_argument('task_id', type=int, help = "id of the task to update")
update_parser.add_argument('task', help = "new description of the task")

mark_parser = subparsers.add_parser('mark', help = "mark a task as todo, in-progress or complete")
mark_parser.add_argument('task_id', type=int, help = "id of the task to mark")
mark_parser.add_argument('status', choices=['todo', 'in-progress', 'complete'], help='status of the task')

args = parser.parse_args()

if args.command == "add":
    task_id = add_task(args.task)
    print(f"Task added: {args.task} (ID: {task_id})")

elif args.command == "list":
    print("Listing tasks:")
    list_tasks(args.todo, args.done, args.in_progress)

elif args.command == "delete":
    print(f"Deleting task ID: {args.task_id}")
    delete_task(args.task_id)

elif args.command == "update":
    print(f"Updating task ID: {args.task_id} to '{args.task}'")
    update_task(args.task_id, args.task)

elif args.command == "mark":
    print(f"Marking task ID: {args.task_id} as '{args.status}'")
    mark_task(args.task_id, args.status)
