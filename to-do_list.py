# making an empty list.
task = []
done_task = []

# Creating a menu for the list.
def menu ():
    print("    To-do list    ")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as done")

# defining the actions of each choice.
def action():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            mark_task_as_done()
        else:
            print('Invalid choice!')

# making logic of adding task.
def add_task():
    while True:
        user_input = input('Enter the task: ')
        if user_input.lower() == 'done':
            break
        else:
            task.append(user_input)
            print('Task added successfully!') 

# making logic of viewing task.
def view_task():
    print('Task that should be done: ')
    for index, tasks in enumerate(task, start=1):
        print(index, tasks)

# makind logic for done task.
def mark_task_as_done():
    while True:
        task_status = input('Enter the task number you have done: ')
        if task_status.lower() == 'd':
            for index, tasks in enumerate(done_task, start=1):
                print(index, tasks)
            break
        if task_status.isdigit():
            task_status = int(task_status)
            if task_status <= len(task):
                done_task.append(task.pop(task_status - 1))
                print('Task marked as done!')
            else:
                print('Invalid task number!')

action()