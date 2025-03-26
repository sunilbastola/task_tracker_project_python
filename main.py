'''
Task_Tracker Pipeline:

Create a function to add task(description) from User.
Assign ID to each tasks.
Update the task to tasks list when writing update.
Assign CreatedAt and updatedAt time to the tasks.
Mark tasks based on the task is (to-do, in progress or done).
list all the tasks.
list tasks by progress.
Make sure to update to JSON when adding and updating tasks.

'''

all_tasks = []
tasks_counter = 0
task_progress = ["to-do", "in-progress", "done"]
task_id = []

def user_input(task):
    user_given_task = input("What do you want to do ? \nPlease add update or delete the tasks")
    if user_given_task == "add" + {}:
        add_task
    elif user_given_task == "update" + {}:
        update_task
    elif user_given_task == "delete" + {}:
        delete_task

def add_task():
    task = input("What do you want to do ?")
    all_tasks.append(task)
    tasks_counter += 1
    created_time = XX

def update_task():
    task = input("What do you want to do ?")
    all_tasks.append(task)
    updated_time = None

def delete_task():
    all_tasks.pop(task_id)

def task_progress():

    if task_progress == task_progress[0]:
        return None