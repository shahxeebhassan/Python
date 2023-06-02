from tkinter import *

class TaskManager(Frame):

    def __init__(self, master):
        super().__init__(master)

        # Create the widgets
        self.task_list = Listbox()
        self.add_task_button = Button(text="Add Task")
        self.remove_task_button = Button(text="Remove Task")
        self.show_all_tasks_button = Button(text="Show All Tasks")

        # Layout the widgets
        self.task_list.pack()
        self.add_task_button.pack()
        self.remove_task_button.pack()
        self.show_all_tasks_button.pack()

        # Bind the buttons to the appropriate functions
        self.add_task_button.config(command=self.add_task)
        self.remove_task_button.config(command=self.remove_task)
        self.show_all_tasks_button.config(command=self.show_all_tasks)

    def add_task(self):
        # Get the task from the user
        task = input("Enter task: ")

        # Add the task to the list
        self.task_list.insert(END, task)

    def remove_task(self):
        # Get the index of the task to remove from the user
        index = int(input("Enter the index of the task to remove: "))

        # Remove the task from the list
        self.task_list.delete(index)

    def show_all_tasks(self):
        # Print all of the tasks in the list
        for task in self.task_list.get(0, END):
            print(task)

if __name__ == "__main__":
    root = Tk()
    root.title("Task Manager")
    root.geometry("300x400")
    task_manager = TaskManager(root)
    task_manager.pack()
    root.mainloop()
