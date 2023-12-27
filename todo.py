import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class App():
    def __init__(self):
        self.root = tk.Tk()

        # app info
        self.root.geometry("300x300")
        self.root.title("To Do List")
        self.root.wm_iconphoto(False, tk.PhotoImage(file = "icon/goofy.png"))

        # app frame to hold all widgets
        self.frame = tk.Frame(self.root, background="white")
        self.frame.pack(fill="both", expand=True)

        # title text
        self.Title = ttk.Label(self.frame, text="To Do:", background="white", font=("Gotham", 30))
        self.Title.grid(row=0, column=0)

        # enter task
        self.taskEntry = ttk.Entry(self.frame)
        self.taskEntry.grid(row=1, column=0, columnspan=2, sticky="EW", padx=(5, 5))

        # set task
        self.setTaskButton = ttk.Button(self.frame, text="Enter", command=self.placeTask)
        self.setTaskButton.grid(row=1, column=2)

        # list of tasks
        self.tasks = tk.Listbox(self.frame, selectmode=tk.SINGLE, font=("Bahnscrift Light", 10))
        self.tasks.grid(row=2, column=0, columnspan=3, sticky="EW", padx=(5,5), pady=5)

        # edit task
        self.editTask = ttk.Button(self.frame, text ="Edit", command=self.edit)
        self.editTask.grid(row=3,column=0, sticky="EW")

        # delete task
        self.tasksDelete = ttk.Button(self.frame, text="Delete", command=self.deleteSelection)
        self.tasksDelete.grid(row=3, column=1, sticky="EW")

        # reset all tasks
        self.resetTasks = ttk.Button(self.frame, text="Reset List", command=self.reset)
        self.resetTasks.grid(row=3, column=2, sticky="EW")

        self.root.mainloop()

    def placeTask(self): # to place taskEntry input in tasks
        task = self.taskEntry.get()

        if task and (task not in self.tasks.get(0, tk.END)): # if there is user input in taskEntry and not a repeat
            self.tasks.insert(tk.END, task)
            self.taskEntry.delete(0, tk.END)

        elif task in self.tasks.get(0, tk.END): # else if there is a repeat
            messagebox.showinfo("Duplicate Task", "Task Already Exists", parent=self.frame)

    def edit(self): # edits selected task
        selectedTaskIndex = self.tasks.curselection()
        if selectedTaskIndex: # if user has selected a task indicated w/ blue outline
            selectedTask = self.tasks.get(selectedTaskIndex)
            editedTask = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=selectedTask, parent=self.frame)

            if editedTask != None: # if user enters something into the simpledialog.askstring
                self.tasks.delete(selectedTaskIndex)
                self.tasks.insert(selectedTaskIndex, editedTask)

    def deleteSelection(self): # deletes selected task
        selectedTask = self.tasks.curselection()
        if selectedTask:
            self.tasks.delete(selectedTask)

    def reset(self):# deletes all tasks in tasks
        self.tasks.delete(0, tk.END)

if __name__ == "__main__": # runs app
    App()