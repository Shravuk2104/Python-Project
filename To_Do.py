# todo_app.py
from task_manager import TaskManager
from utils import print_menu, get_integer_input

def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = get_integer_input("Choose an option: ")

        if choice == 1:
            task = input("Enter the task: ")
            try:
                task_manager.add_task(task)
                print("Task added successfully.")
            except ValueError as e:
                print(e)

        elif choice == 2:
            print("Tasks:")
            print(task_manager.view_tasks())

        elif choice == 3:
            print("Tasks:")
            print(task_manager.view_tasks())
            try:
                task_index = get_integer_input("Enter the task number to remove: ") - 1
                task_manager.remove_task(task_index)
                print("Task removed successfully.")
            except (IndexError, ValueError) as e:
                print(e)

        elif choice == 4:
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
