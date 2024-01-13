prompt="Enter a To-Do item: "

todos=[]

while True:
    todo=input(prompt)
    todos.append(todo)
    print("To-Do list:", todos)