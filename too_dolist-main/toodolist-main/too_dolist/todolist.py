class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def get_tasks(self):
        return self.tasks

# Contoh penggunaan
if __name__ == "__main__":
    my_todo_list = TodoList()

    my_todo_list.add_task("Study for the exam")
    my_todo_list.add_task("Buy groceries")
    my_todo_list.add_task("Write a report")

    print("Tasks:", my_todo_list.get_tasks())

    my_todo_list.remove_task("Buy groceries")

    print("Updated Tasks:", my_todo_list.get_tasks())
