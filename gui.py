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
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()

