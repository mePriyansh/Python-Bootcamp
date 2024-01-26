todos=[]
while True:
    action = input("Add or Show or Edit or Exit ? ")
    action=action.strip()

    match action:
        case "Add":
            todo = input("Enter a to-do item: ")
            todos.append(todo)
        case "Show":
            for index, items in enumerate(todos):
                print(index, '-', items)
        case "Edit":
            number = int(input("Enter the number of the item to edit: "))
            number=number-1
            new_todo = input("Enter the new to-do item: ")
            todos[number] = new_todo
        case "Exit":
            break
        case _:
            print("Invalid action")