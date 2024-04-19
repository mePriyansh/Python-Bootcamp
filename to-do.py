while True:
    action = input("Add or Show or Edit or Complete or Exit? ")
    action=action.strip()

    match action:
        case "Add":
            todo = input("Enter a to-do item: ") + "\n"

            '''file=open("todos.txt","r")       To read file and append the new item
            todos=file.readlines()
            file.close()'''

            with open("todos.txt","r") as file:             #To read file but don't need to close the file
                todos = file.readlines()

            todos.append(todo)
            
            '''file=open("todos.txt","w")  
            file.writelines(todos)
            file.close()'''

            with open("todos.txt","w") as file:
                file.writelines(todos)             
        
        case "Show":

            with open("todos.txt","r") as file:             #To read file but don't need to close the file
                todos = file.readlines()
            
            ''' To remove the \n from the list using for loop
            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            '''
            #new_todos = [item.strip('\n') for item in todos] # List comprehension to remove the \n from the list
            
            for index, items in enumerate(todos):
                items = items.strip('\n')
                row = f"{index+1}-{items}"
                print(row)
        
        case "Edit":
            number = int(input("Enter the number of the item to edit: "))
            number=number-1

            with open("todos.txt","r") as file:             #To read file but don't need to close the file
                todos = file.readlines()

            new_todo = input("Enter the new to-do item: ")
            todos[number] = new_todo+"\n"

            with open("todos.txt","w") as file:
                file.writelines(todos) 
        
        case "Complete":
            number = int(input("Enter the number of the item to complete: "))
            number=number-1

            with open("todos.txt","r") as file:             #To read file but don't need to close the file
                todos = file.readlines()

            todo_to_complete = todos[number]
            todos.pop(number)

            with open("todos.txt","w") as file:
                file.writelines(todos)

            message = f"{todo_to_complete.strip()} is completed!"
            print(message)
        
        case "Exit":
            break
        
        case _:
            print("Invalid action")