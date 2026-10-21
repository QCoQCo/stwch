import json
import os
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

BG = "black"
TASK_FG = "yellow"
DONE_FG = "gray50"
TASK_FONT = ("Helvetica", 13)
DONE_FONT = ("Helvetica", 13, "overstrike")
SAVE_PATH = Path.home() / ".stopwatch_todo.json"
SCROLL_STEP = 20


def load_tasks(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    if not isinstance(data, list):
        raise ValueError("task file must contain a list")
    return [
        {"text": str(item["text"]), "done": bool(item.get("done", False))}
        for item in data
        if isinstance(item, dict) and "text" in item
    ]


def save_tasks(tasks, path):
    # 임시 파일에 쓴 뒤 교체해서, 저장 도중 종료돼도 기존 파일이 깨지지 않게 함
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


class ToDoListApp:
    def __init__(self, R, save_path=SAVE_PATH):
        self.R = R
        self.R.title("To-Do List")
        R.geometry("600x300")
        R.configure(bg=BG)
        self.sp = Path(save_path)

        self.T = []

        self.F = tk.Frame(R, bg=BG)
        self.F.pack(pady=10)

        self.te = tk.Entry(self.F, width=50)
        self.te.pack(side="left", padx=5)
        self.te.bind("<Return>", lambda e: self.add_task())
        self.te.focus_set()

        self.tb = tk.Button(self.F, text="Add Task", command=self.add_task)
        self.tb.pack(side="left")

        self.lf = tk.Frame(R, bg=BG)
        self.lf.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.cv = tk.Canvas(self.lf, bg=BG, highlightthickness=0, yscrollincrement=SCROLL_STEP)
        self.sb = tk.Scrollbar(self.lf, orient="vertical", command=self.cv.yview)
        self.cv.configure(yscrollcommand=self.sb.set)
        self.sb.pack(side="right", fill="y")
        self.cv.pack(side="left", fill="both", expand=True)

        self.tf = tk.Frame(self.cv, bg=BG)
        tw = self.cv.create_window((0, 0), window=self.tf, anchor="nw")
        self.tf.bind("<Configure>", lambda e: self.cv.configure(scrollregion=self.cv.bbox("all")))
        self.cv.bind("<Configure>", lambda e: self.cv.itemconfigure(tw, width=e.width))

        # 창(toplevel)에 바인딩하면 작업 항목 위에서도 휠이 동작하고 다른 창에는 영향이 없음
        R.bind("<MouseWheel>", self.on_wheel)
        R.bind("<Button-4>", self.on_wheel)
        R.bind("<Button-5>", self.on_wheel)
        self.ta = 0
        try:
            R.bind("<TouchpadScroll>", self.on_touchpad)  # Tk 9+
        except tk.TclError:
            pass

        for item in self.load():
            self.create_task(item["text"], item["done"])

    def load(self):
        try:
            return load_tasks(self.sp)
        except (OSError, ValueError) as e:
            bk = self.sp.with_name(self.sp.name + ".bak")
            try:
                os.replace(self.sp, bk)
                detail = f"The file was moved to:\n{bk}"
            except OSError:
                detail = "The file could not be backed up and will be overwritten on the next save."
            messagebox.showwarning("Warning", f"Could not read saved tasks ({e}).\n{detail}", parent=self.R)
            return []

    def save(self):
        data = [{"text": st.get(), "done": bool(chk.get())} for task, st, chk in self.T]
        try:
            save_tasks(data, self.sp)
        except OSError as e:
            messagebox.showerror("Error", f"Failed to save tasks:\n{e}", parent=self.R)

    def add_task(self):
        tx = self.te.get().strip()
        if tx:
            self.create_task(tx, False)
            self.te.delete(0, tk.END)
            self.save()
            self.cv.update_idletasks()
            self.cv.yview_moveto(1.0)
        else:
            messagebox.showwarning("Warning", "You must enter a task.", parent=self.R)

    def create_task(self, tx, done):
        task = tk.Frame(self.tf, bg=BG)
        task.pack(fill="x", pady=2)

        st = tk.StringVar(value=tx)
        te = tk.Entry(task, textvariable=st, state="readonly", width=40,
                      relief="flat", highlightthickness=0, readonlybackground=BG)
        te.pack(side="left", padx=5)

        chk = tk.IntVar(value=int(done))
        sel = tk.Checkbutton(task, variable=chk, command=lambda: self.toggle_task(task, chk),
                             bg=BG, activebackground=BG, highlightthickness=0)
        sel.pack(side="left")

        self.T.append((task, st, chk))
        self.apply_style(task, chk)

    def toggle_task(self, task, chk):
        self.apply_style(task, chk)
        self.save()

    def apply_style(self, task, chk):
        te = next(w for w in task.winfo_children() if isinstance(w, tk.Entry))
        if chk.get():
            te.config(fg=DONE_FG, font=DONE_FONT)
            if not any(isinstance(w, tk.Button) for w in task.winfo_children()):
                del_b = tk.Button(task, text="Delete", command=lambda: self.delete_task(task))
                del_b.pack(side="left", padx=5)
        else:
            te.config(fg=TASK_FG, font=TASK_FONT)
            for widget in task.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.destroy()

    def delete_task(self, task):
        task.destroy()
        self.T = [(t, var, chk) for t, var, chk in self.T if t != task]
        self.save()

    def on_wheel(self, event):
        # 플랫폼/Tk 버전마다 delta 단위가 달라서 방향만 보고 한 칸씩 스크롤
        if event.num == 4 or event.delta > 0:
            self.cv.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.cv.yview_scroll(1, "units")

    def on_touchpad(self, event):
        # delta 하위 16비트가 세로 이동량(px). 조금씩 들어오므로 모아서 한 칸 단위로 스크롤
        dy = event.delta & 0xFFFF
        if dy >= 0x8000:
            dy -= 0x10000
        self.ta -= dy
        steps = int(self.ta / SCROLL_STEP)
        if steps:
            self.ta -= steps * SCROLL_STEP
            self.cv.yview_scroll(steps, "units")


if __name__ == "__main__":
    R = tk.Tk()
    app = ToDoListApp(R)
    R.mainloop()
