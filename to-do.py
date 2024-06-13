#from functions import get_todos, write_todos

import functions

while True:
    action = input("Add or Show or Edit or Complete or Exit? ")
    action = action.strip()

    if action.startswith("Add"):
        todo = action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)
        print(f"{todo} is added!")

    elif action.startswith("Show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos, 1):
            print(f"{index}-{item.strip()}")

    elif action.startswith("Edit"):
        try:
            number = int(action[5:])
            print(number)
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter the new to-do item: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Not a valid command!!")
            continue

    elif action.startswith("Complete"):
        try:
            number = int(action[9:])
            number -= 1

            todos = functions.get_todos()

            todo_to_complete = todos[number]
            todos.pop(number)

            functions.write_todos(todos)

            message = f"{todo_to_complete.strip()} is completed!"
            print(message)
        except IndexError:
            print("No item found with that number!!")
            continue

    elif action.startswith("Exit"):
        break

    else:
        print("Invalid action")
