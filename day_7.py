tasks = []

while True:
    print("1) Add a task")
    print("2) View tasks")
    print("3) Mark a task as done")
    print("4) Remove a task")
    print("5) Quit")
    choice = input("Choice: ")

    if choice == "1":
        task_text = input("Enter the task: ")
        tasks.append({"task":task_text, "done":False})
        print("Task added!")
    elif choice == "2":
        if len(tasks)==0:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks):
                status = "DONE" if t["done"]else""
                print(f"{i+1}.[{status}]{t['task']}")
    elif choice =="3":
        for i, t in enumerate(tasks):
            status = "DONE" if t["done"]else""
            print(f"{i+1}.[{status}]{t['task']}")
        num = input("Which task number is done?")
        if num.isdigit():
            index = int(num)-1
            if 0<=index<len(tasks):
                tasks[index]["done"] = True
                print("Marked as done!")
            else:
                print("Invalid number.")
        else:
            print("That's not a number.")
    elif choice == "4":
        for i, t in enumerate(tasks):
            status = "DONE" if t["done"]else""
            print(f"{i+1}.[{status}]{t['task']}")
        num = input("Which task number to remove?")
        if num.isdigit():
            index = int(num)-1
            if 0<=index<len(tasks):
                removed = tasks.pop(index)
                print("Removed: ", removed["task"])
            else:
                print("Invalid number.")
        else:
            print("That's not a number.")

    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid choice")