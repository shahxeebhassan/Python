import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the widgets
        self.task_list = tk.Listbox(self, font=('Arial', 12))
        self.add_task_button = tk.Button(self, text="Add Task", font=('Arial', 12), command=self.add_task)
        self.remove_task_button = tk.Button(self, text="Remove Task", font=('Arial', 12), command=self.remove_task)
        self.show_all_tasks_button = tk.Button(self, text="Show All Tasks", font=('Arial', 12), command=self.show_all_tasks)

        # Layout the widgets
        self.task_list.pack(padx=10, pady=10)
        self.add_task_button.pack(pady=5)
        self.remove_task_button.pack(pady=5)
        self.show_all_tasks_button.pack(pady=5)

    def add_task(self):
        # Get the task from the user
        task = simpledialog.askstring("Add Task", "Enter task:")

        if task:
            # Add the task to the list
            self.task_list.insert(tk.END, task)

    def remove_task(self):
        # Get the selected task from the list
        selection = self.task_list.curselection()

        if selection:
            # Remove the selected task from the list
            self.task_list.delete(selection)

    def show_all_tasks(self):
        # Print all of the tasks in the list
        tasks = self.task_list.get(0, tk.END)
        messagebox.showinfo("All Tasks", "\n".join(tasks))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("300x400")
    root.resizable(False, False)
    root.configure(background="#F0F0F0")

    task_manager = TaskManager(root)
    task_manager.pack()

    root.mainloop()
