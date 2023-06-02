import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the widgets
        self.task_list = tk.Listbox(self, font=('Arial', 12))
        self.add_task_button = tk.Button(self, text="Add Task", font=('Arial', 12), command=self.add_task, bg="#4CAF50", fg="white", padx=10)
        self.remove_task_button = tk.Button(self, text="Remove Task", font=('Arial', 12), command=self.remove_task, bg="#FF5722", fg="white", padx=10)
        self.remove_all_tasks_button = tk.Button(self, text="Remove All Tasks", font=('Arial', 12), command=self.remove_all_tasks, bg="#FF5722", fg="white", padx=10)
        self.show_all_tasks_button = tk.Button(self, text="Show All Tasks", font=('Arial', 12), command=self.show_all_tasks, bg="#2196F3", fg="white", padx=10)

        # Layout the widgets
        self.task_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.add_task_button.pack(pady=5, padx=10, side=tk.LEFT)
        self.remove_task_button.pack(pady=5, padx=10, side=tk.LEFT)
        self.remove_all_tasks_button.pack(pady=5, padx=10, side=tk.LEFT)
        self.show_all_tasks_button.pack(pady=5, padx=10, side=tk.LEFT)

        # Set background color
        self.configure(background="#F0F0F0")

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

    def remove_all_tasks(self):
        # Remove all tasks from the list
        self.task_list.delete(0, tk.END)

    def show_all_tasks(self):
        # Print all of the tasks in the list
        tasks = self.task_list.get(0, tk.END)
        messagebox.showinfo("All Tasks", "\n".join(tasks))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("400x300")
    root.resizable(False, False)

    task_manager = TaskManager(root)
    task_manager.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
