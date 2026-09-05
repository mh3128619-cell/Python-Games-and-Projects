message="""
1)Add task to a list
2)Remove task from the list
3)Mark task as completed
4)View all tasks
5)Quit
"""
task_list = []

def add_task():
    task = input("Enter the task to add: ").strip()
    if task:
        task_list.append({"task": task, "completed": False})
        print(f'Task "{task}" added to the list.')
    else:
        print("No task entered. Please try again.")

def remove_task():
    if not task_list:
        print("No tasks available to remove.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(task_list):
            removed_task = task_list.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" removed from the list.')
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def mark_task_completed():
    if not task_list:
        print("No tasks available to mark as completed.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(task_list):
            task_list[task_number - 1]["completed"] = True
            print(f'Task "{task_list[task_number - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def view_tasks():
    if not task_list:
        print("No tasks in the list.")
        return

    print("\nTask List:")
    for index, task in enumerate(task_list, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")
    print()

while True:
    print(message)
    choice = input("Enter your choice (1-5): ").lower().strip()
    
    if choice == "1" or choice == "add":
        add_task()
    elif choice == "2" or choice == "remove":
        remove_task()
    elif choice == "3" or choice == "mark":
        mark_task_completed()
    elif choice == "4" or choice == "view":
        view_tasks()
    elif choice == "5" or choice == "quit":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option from 1 to 5.")
