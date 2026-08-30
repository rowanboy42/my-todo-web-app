FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Return a list of to-do items from the text file. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a list of to-do items to the text file. """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("You can run code not to be shared as module here")