tasks = []
def addtask():
    print("\n Add New Task ")
    name = input("Enter task name: ")
    mins = input("Enter time required (in minutes): ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append([name, mins, priority, "Pending"])
    print("Task added successfully!\n")
def viewtasks():
    print("\n Your Tasks")
    if len(tasks) == 0:
        print("No tasks added yet.\n")
        return
    for i in range(len(tasks)):
        t = tasks[i]
        print(f"{i + 1}. {t[0]} | {t[1]} mins | Priority: {t[2]} | Status: {t[3]}")
    print()
def updatetask():
    viewtasks()
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to update: "))
    if 1 <= num <= len(tasks):
        tasks[num - 1][3] = "Completed"
        print("Task marked as Completed!\n")
    else:
        print("Invalid task number!\n")
def deletetask():
    viewtasks()
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted!\n")
    else:
        print("Invalid task number!\n")
def totalstudytime():
    total = 0
    for i in range(len(tasks)):
        total += int(tasks[i][1])
    print(f"\n Total Planned Study Time: {total} minutes \n")
def highestpriority():
    if len(tasks) == 0:
        print("\n No tasks to analyze.\n")
        return
    list2 = []
    for i in range(len(tasks)):
        if tasks[i][2].lower() == "high":
            list2.append(tasks[i])
    if len(list2) == 0:
        print("\n No High Priority tasks.\n")
    else:
        print("\n High Priority Tasks ")
        for i in list2:
            print(f"- {i[0]} ({i[1]} mins)")
        print()
def planner():
    while True:
        print(" STUDY PLANNER ")
        print("1. Enter Your Task ")
        print("2. View Your Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Total Study Time")
        print("6. Show Priority Of Tasks")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            addtask()
        elif choice == "2":
            viewtasks()
        elif choice == "3":
            updatetask()
        elif choice == "4":
            deletetask()
        elif choice == "5":
            totalstudytime()
        elif choice == "6":
            highestpriority()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")
planner()
