from modules import functions
import FreeSimpleGUI as sg

label= sg.Text("Enter your task")
input_box=sg.InputText(tooltip="Enter your task", key="todo")
add_button=sg.Button("Add",tooltip="Add your task")
listbox=sg.Listbox(values=functions.get_todos(), key='todos', 
                   enable_events=True, size=[40,10])
edit_button=sg.Button("Edit", tooltip="Edit your task")

window=sg.Window("My To-Do App", 
                 layout=[[label],[input_box,add_button], [listbox, edit_button]],
                 font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            
        case "Edit":
            todo_to_edit =values['todos'][0]
            new_todo=values['todo']
            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)                    #to update list during run-time

        case "todos":
            window['todo'].update(value=values['todos'][0])         #to update list during run-time   

        case sg.WIN_CLOSED:                                         #to close the window w/o error
            break                                               

window.close()

