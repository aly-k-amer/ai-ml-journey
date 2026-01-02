# Task Manager - Day 1 Project
# Goal: Add tasks and view them
filename = "tasks.txt"
def add_task():
    description = input("Enter task description: ")
    
    with open(filename, "a") as file:
        file.write(description + "\n")
        print("Task added successfully.")

def view_tasks():
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
                return
            print("Your Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def main():
    while True:
        print("=== Simple Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    