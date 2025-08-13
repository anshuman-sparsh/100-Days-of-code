import os

FILENAME = "Day 78/tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("-----------------------\n")

def add_task(tasks):
    task_description = input("Enter the new task: ")
    tasks.append(f"[ ] {task_description}")
    save_tasks(tasks)
    print(f"Task '{task_description}' added successfully.")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to mark as done: "))
        if 1 <= task_number <= len(tasks):
            task_index = task_number - 1
            if "[ ]" in tasks[task_index]:
                tasks[task_index] = tasks[task_index].replace("[ ]", "[x]", 1)
                save_tasks(tasks)
                print(f"Task {task_number} marked as done.")
            else:
                print("That task is already marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()