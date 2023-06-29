def get_tasks():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        return tasks


def write_tasks(tasks):
    with open("todo.txt", "w") as file:
        file.writelines(tasks)
