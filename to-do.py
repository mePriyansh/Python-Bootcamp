todos=[]
while True:
    action = input("Add or Show or Exit ? ")

    match action:
        case "Add":
            todo = input("Enter a to-do item: ")
            todos.append(todo)
        case "Show":
            print("To-Do list:", todos)
        case "Exit":
            break