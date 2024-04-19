while True:
    action = input("Add or Show or Edit or Complete or Exit? ")
    action=action.strip()

    match action:
        case "Add":
            todo = input("Enter a to-do item: ") + "\n"

            file=open("todos.txt","r")
            todos=file.readlines()
            file.close()

            todos.append(todo)
            
            file=open("todos.txt","w")  
            file.writelines(todos)
            file.close()
        
        case "Show":
            file=open("todos.txt","r")
            todos=file.readlines()
            file.close()

            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            
            for index, items in enumerate(new_todos):
                row = f"{index+1}-{items}"
                print(row)
        
        case "Edit":
            number = int(input("Enter the number of the item to edit: "))
            number=number-1
            new_todo = input("Enter the new to-do item: ")
            todos[number] = new_todo
        
        case "Complete":
            number = int(input("Enter the number of the item to complete: "))
            number=number-1
            todos.pop(number)
        
        case "Exit":
            break
        
        case _:
            print("Invalid action")