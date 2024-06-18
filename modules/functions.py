FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the to-do list from the file 
    and return it as a list"""

    with open(filepath, "r") as file_local:
         todos_local = file_local.readlines()
         return todos_local

def write_todos(todos_arg,filepath=FILEPATH):

    """Write the to-do list to the file"""

    with open(filepath, "w") as file:
        file.writelines(todos_arg)
