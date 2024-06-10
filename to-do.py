def get_todos(filepath):
    with open(filepath, "r") as file_local:
         todos_local = file_local.readlines()
         return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

while True:
    action = input("Add or Show or Edit or Complete or Exit? ")
    action = action.strip()

    if action.startswith("Add"):
        todo = action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + "\n")

        write_todos("todos.txt", todos)
        print(f"{todo} is added!")

    elif action.startswith("Show"):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos, 1):
            print(f"{index}-{item.strip()}")

    elif action.startswith("Edit"):
        try:
            number = int(action[5:])
            print(number)
            number -= 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter the new to-do item: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)
        except ValueError:
            print("Not a valid command!!")
            continue

    elif action.startswith("Complete"):
        try:
            number = int(action[9:])
            number -= 1

            todos = get_todos("todos.txt")

            todo_to_complete = todos[number]
            todos.pop(number)

            write_todos("todos.txt", todos)

            message = f"{todo_to_complete.strip()} is completed!"
            print(message)
        except IndexError:
            print("No item found with that number!!")
            continue

    elif action.startswith("Exit"):
        break

    else:
        print("Invalid action")
