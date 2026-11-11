task = []

while True:
    print("1) Add 2) Remove 3) View 4) Quit")
    choice = input("Choose an option: ")
    if choice == "1":
       new_task = input("Enter a task: ")
       task.append(new_task)
    elif choice == "2":
        for i in range(len(task)):
            print(i+1, task[i])
            remove_num = int(input("Enter the number of the taks to remove: "))
            task.pop(remove_num-1)
    elif choice == "3":
        for i in range(len(task)):
            print(i+1, task[i])
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
     
    