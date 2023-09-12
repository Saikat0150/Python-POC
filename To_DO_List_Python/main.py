def to_do_list():
    tasks = []
    while True:
        print("""******To-Do List******
        1. Add Tasks
        2. View Tasks
        3. Mark Task as completed
        4. Remove Task
        5. Exit
        """)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            again = 'y'
            while again == 'y':
                task = input("Entre the task: ")
                tasks.append(task)
                print("Task added successfully..")
                again = input("Do you want to add another task (Yes=Y or No=N): ").lower()

        elif choice == 2:
            if tasks:
                print("Tasks")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")
            else:
                print("No task found..")
        elif choice == 3:
            index = int(input("Enter the number of the task to mark as completed: "))
            if 1 <= index <= len(tasks):
                tasks[index - 1] += " (Completed)"
                print("Task marked as completed..")
            else:
                print("Invalid task..")
        elif choice == 4:
            index = int(input("Enter the number of the task to remove: "))
            if 1 <= index <= len(tasks):
                del tasks[index - 1]
                print("Task removed successfully..")
            else:
                print("Invalid task. Please try again..")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again..")

        print()

    print("Thank You")


to_do_list()
