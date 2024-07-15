# Initialize an empty list to store tasks
todo_list = []

# Function to add a task
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Main function to handle user input
def main():
    while True:
        print("\nTo-Do List Options:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting the to-do list program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
