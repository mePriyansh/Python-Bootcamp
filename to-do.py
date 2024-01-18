todos=[]
while True:
    action = input("Add or Show or Exit ? ")
    action=action.strip()

    match action:
        case "Add":
            todo = input("Enter a to-do item: ")
            todos.append(todo)
        case "Show":
            for items in todos:
                print(items)
        case "Exit":
            break
        case _:
            print("Invalid action")