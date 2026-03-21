tasks=[]
while True:
    print("\nTO DO LIST")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        tasks.append(input("Enter task name:"))
        print("Task successfully added.")

    elif choice=="2":
        if len(tasks)==0:
            print("No tasks in the list")
        else:
            print("Your Tasks:")
            i=1
            for task in tasks:
                print(i,"-",task)
                i=i+1

    elif choice=="3":
        if len(tasks)==0:
            print("task list is empty")
        else:
            num=int(input("Enter task number to delete:"))
            if 0 < num <= len(tasks):
                tasks.pop(num-1)
                print("Task successfully deleted.1")
            else:
                print("wrong choice")

    elif choice=="4":
        print("Program Closed")
        break
    else:
        print("Please enter correct choice")