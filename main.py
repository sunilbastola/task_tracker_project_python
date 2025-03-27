# Import the relevant libraries:
import sys
import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def main():
    if len(sys.argv) < 2:
        print("Usage: task_cli [command]")
        return
    
    command = sys.argv[1].lower()
    tasks = load_tasks()

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing Task Description")
            return
        add_task(tasks, " ".join(sys.argv[2:]))
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Missing task ID or description")
            return
        update_task(tasks, int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            return
        delete_task(tasks, int(sys.argv[2]))
    elif command.startswith("mark-"):
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            return
        status = command.split("-")[-1]
        mark_task(tasks, int(sys.argv[2]), status)
    elif command == "list":
        list_tasks(tasks, sys.argv[2] if len(sys.argv) > 2 else None)
    else:
        print("Unknown Command. Please use add, update, delete, mark-todo, mark-in-progress, mark-done, or list.")

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks, description):
    new_task = {
        "id": max([task["id"] for task in tasks] + [0]) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(tasks, task_id, new_description):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        task["description"] = new_description
        task["updatedAt"] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully")
    else:
        print(f"Task {task_id} not found")

def delete_task(tasks, task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Task {task_id} not found")

def mark_task(tasks, task_id, status):
    if status not in ["todo", "in-progress", "done"]:
        print(f"Invalid status: {status}")
        return
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        task["status"] = status
        task["updatedAt"] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task {task_id} marked as {status}")
    else:
        print(f"Task {task_id} not found")

def list_tasks(tasks, status_filter=None):
    filtered = [t for t in tasks if not status_filter or t["status"] == status_filter]
    for task in filtered:
        print(f"{task['id']}: {task['description']} [{task['status']}]")

if __name__ == "__main__":
    main()