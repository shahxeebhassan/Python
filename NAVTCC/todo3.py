import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the widgets
        self.task_list = tk.Listbox(self, font=('Arial', 12), bg="white")
        self.add_task_button = tk.Button(self, text="Add Task", font=('Arial', 12), command=self.add_task, bg="#4CAF50", fg="white", padx=10)
        self.remove_task_button = tk.Button(self, text="Remove Task", font=('Arial', 12), command=self.remove_task, bg="#FF5722", fg="white", padx=10)
        self.show_all_tasks_button = tk.Button(self, text="Show All Tasks", font=('Arial', 12), command=self.show_all_tasks, bg="#2196F3", fg="white", padx=10)

        # Layout the widgets
        self.task_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.add_task_button.pack(pady=5, padx=10, side=tk.LEFT)
        self.remove_task_button.pack(pady=5, padx=10, side=tk.LEFT)
        self.show_all_tasks_button.pack(pady=5, padx=10, side=tk.LEFT)

        # Set background color for the task panel
        self.task_list.configure(bg="#F0F0F0")

    def add_task(self):
        # Get the task from the user
        task = simpledialog.askstring("Add Task", "Enter task:")

        if task:
            if task not in self.task_list.get(0, tk.END):
                # Add the task to the list
                self.task_list.insert(tk.END, task)
            else:
                messagebox.showwarning("Duplicate Task", "Task already exists!")

    def remove_task(self):
        # Get the selected task from the list
        selection = self.task_list.curselection()

        if selection:
            # Remove the selected task from the list
            self.task_list.delete(selection)

    def show_all_tasks(self):
        # Get all of the tasks in the list
        tasks = self.task_list.get(0, tk.END)

        if tasks:
            # Create a new dialog box to display the tasks
            tasks_dialog = tk.Toplevel(self)
            tasks_dialog.title("All Tasks")
            tasks_dialog.geometry("300x200")
            tasks_dialog.configure(background="#ECECEC")

            # Create a frame to contain the tasks
            tasks_frame = tk.Frame(tasks_dialog, bg="#ECECEC")
            tasks_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            # Create a label to show the tasks
            tasks_label = tk.Label(tasks_frame, text="\n".join(tasks), font=('Arial', 12), bg="#ECECEC")
            tasks_label.pack(padx=10, pady=10)
        else:
            messagebox.showinfo("All Tasks", "No tasks to show.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("400x300")
    root.resizable(False, False)
    root.configure(background="#F0F0F0")

    task_manager = TaskManager(root)
    task_manager.pack(fill=tk.BOTH, expand=True)

    root.mainloop()