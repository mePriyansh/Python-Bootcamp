from modules import functions
import FreeSimpleGUI as sg

label= sg.Text("Enter your task")
input_box=sg.InputText(tooltip="Enter your task")
add_button=sg.Button("Add",tooltip="Add your task")

window=sg.Window("My To-Do App",layout=[[label],[input_box,add_button]])
window.read()
window.close()

