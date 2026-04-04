tasks = ["Eat food ", "Learn JavaScript"]

while True:
    print("\nTodo App")
    print("1. View tasks")
    print("2. Add tasks")
    print("3. Delete tasks")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == '1' :
        if len(tasks) == 0:
            print("No tasks")
        else:
            # using enumerate
            for i , task in enumerate(tasks):
                print(i+1,task)
    
    elif choice == '2' :
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    
    elif choice == '3' :
        for num,task in enumerate(tasks):
            print(num+1,task)

        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task removed!")

    elif choice == "4":
        break