# Project 3: File-Based To-Do List App
# Goal: Build a command-line To-Do list where tasks are stored in a .txt file and persist across runs.




def add_tasks():
    task = input("Enter your task: ").strip()
    if task:
       with open("Day 20/todo.txt", "a") as f:
        f.write(task + "\n")
        print("Task added!")
    else:
        print("Task cannot be empty.")


def view_all_tasks():
    try:
     with open("Day 20/todo.txt", "r") as f:
        tasks = f.readlines()

     if not tasks:
        print("No tasks found.")
     else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("0 Tasks.")


def remove_task():
    try:
     with open("Day 20/todo.txt") as f:
        tasks = f.read().splitlines()

     if not tasks:
        print("No tasks!")
     else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        num_input = input("Enter the task number to remove: ")

        if num_input.isdigit():
            num = int(num_input)
            if 1 <= num <= len(tasks):
                removed_task = tasks[num - 1]
                tasks.pop(num - 1)  

                with open("Day 20/todo.txt", "w") as f:
                    f.write("\n".join(tasks)) 

                print(f"Removed: {removed_task}")
            else:
                print("Number out of range!")
        else:
            print("Please enter a valid number.")
    except FileNotFoundError:
        print("No such tasks Found.")



def clear_all_tasks():

 confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()

 if confirm in ["yes"]:
    try:
        with open("Day 20/todo.txt", "w") as f:
            pass  
        print("All tasks cleared!")
    except FileNotFoundError:
       print("No file to clear tasks.")
 else:
    print("Deletion cancelled.")


def exit_app():
    print("Exiting To-Do App. Goodbye! 👋")






while True:
    print("\n To-Do List App")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Remove Task by Number")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print("You chose to add a task.")
        add_tasks()
    elif choice == "2":
        print("You chose to view tasks.")
        view_all_tasks()
    elif choice == "3":
        print("You chose to remove a task.")
        remove_task()
    elif choice == "4":
        print("You chose to clear all tasks.")
        clear_all_tasks()
    elif choice == "5":
        exit_app()
        break
    else:
        print("Invalid choice. Please try again.")
