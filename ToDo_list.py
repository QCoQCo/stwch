import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, R):
        self.R = R
        self.R.title("To-Do List")
        R.geometry("600x300")

        self.T = []

        self.F = tk.Frame(R)
        self.F.pack(pady=10)

        self.te = tk.Entry(self.F, width=50)
        self.te.pack(side="left", padx=5)

        self.tb = tk.Button(self.F, text="Add Task", command=self.add_task)
        self.tb.pack(side="left")

        self.tf = tk.Frame(R)
        self.tf.pack(pady=10)

    def add_task(self):
        tx = self.te.get()
        if tx:
            task = tk.Frame(self.tf)
            task.pack(fill="x", pady=2)

            st = tk.StringVar(value=tx)
            te = tk.Entry(task, textvariable=st, state="readonly", width=40,fg='yellow')
            te.pack(side="left", padx=5)

            chk = tk.IntVar()
            sel = tk.Checkbutton(task, variable=chk, command=lambda: self.toggle_task(task, chk))
            sel.pack(side="left")

            self.T.append((task, st, chk))
            self.te.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def toggle_task(self, task, chk):
        if chk.get():
            del_b = tk.Button(task, text="Delete", command=lambda: self.delete_task(task))
            del_b.pack(side="left", padx=5)
        else:
            for widget in task.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.destroy()

    def delete_task(self, task):
        task.destroy()
        self.T = [(t, var, chk) for t, var, chk in self.T if t != task]


if __name__ == "__main__":
    R = tk.Tk()
    app = ToDoListApp(R)
    R.mainloop()