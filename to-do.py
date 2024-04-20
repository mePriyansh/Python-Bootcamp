while True:
    action = input("Add or Show or Edit or Complete or Exit? ")
    action = action.strip()

    if action.startswith("Add"):
        todo = action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        print(f"{todo} is added!")

    elif action.startswith("Show"):

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos, 1):
            print(f"{index}-{item.strip()}")

    elif action.startswith("Edit"):
        number = int(action[5:])
        print(number)
        number -= 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter the new to-do item: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif action.startswith("Complete"):
        number = int(action[9:])
        number -= 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todo_to_complete = todos[number]
        todos.pop(number)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"{todo_to_complete.strip()} is completed!"
        print(message)

    elif action.startswith("Exit"):
        break

    else:
        print("Invalid action")
