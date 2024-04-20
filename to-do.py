while True:
    action = input("Add or Show or Edit or Complete or Exit? ")
    action = action.strip()

    if "Add" in action:
        todo = action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        print(f"{todo} is added!")

    elif "Show" in action:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos, 1):
            print(f"{index}-{item.strip()}")

    elif "Edit" in action:
        number = int(input("Enter the number of the item to edit: "))
        number -= 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter the new to-do item: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "Complete" in action:
        number = int(input("Enter the number of the item to complete: "))
        number -= 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todo_to_complete = todos[number]
        todos.pop(number)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"{todo_to_complete.strip()} is completed!"
        print(message)

    elif "Exit" in action:
        break

    else:
        print("Invalid action")
