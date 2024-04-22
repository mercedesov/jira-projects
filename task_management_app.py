tasks = []


# function to add new task
def add_task():
    name = input("Enter name: ")
    description = input("Enter description: ")
    # checks if already exists or not
    for task in tasks:
        if task['name'] == name:
            print("Task with this name already exists.")
            return
    # if not exist adds new task
    tasks.append({'name': name, 'description': description})
    print("Task added.")


# function to update task
def update_task():
    name = input("Enter new name: ")
    description = input("Enter new description: ")
    # search for task
    for task in tasks:
        if task['name'] == name:
            task['description'] = description
            print("Task updated.")
            return
    print("Task not found.")


# function to list tasks
def list_tasks():
    # checks if there are tasks
    if not tasks:
        print("No tasks found.")
        return
    print("Tasks:")
    # prints list of tasks with name and description
    counter = 1
    for task in tasks:
        print(
            f"{counter}. Name: {task['name']} Description: {task['description']}")
        counter += 1


# function to remove task
def remove_task():
    name = input("Enter task name to remove: ")
    # search for task
    for task in tasks:
        if task['name'] == name:
            # if there remove
            tasks.remove(task)
            print("Task removed.")
            return
    print("Task not found.")


# lets program not to stop after one prompt
while True:
    print("COMMANDS:")
    print("1. ADD")
    print("2. UPDATE")
    print("3. LIST")
    print("4. REMOVE")
    print("5. EXIT")
    command = input("Enter command: ")
    # dealing with commands
    if command == "ADD":
        add_task()
    elif command == "UPDATE":
        update_task()
    elif command == "LIST":
        list_tasks()
    elif command == "REMOVE":
        remove_task()
    elif command == "EXIT":
        print("Exiting.")
        break
    else:
        print("No such command.")
