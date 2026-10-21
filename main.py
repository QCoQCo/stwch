import time
import tkinter as tk
from datetime import datetime
from todo_list import ToDoListApp

BG="black"

class Stopwatch:
    def __init__(self,R):
        self.R=R
        self.R.title("Stopwatch")
        R.geometry("1200x720")
        R.configure(bg=BG)
        self.s_t=None
        self.t_f=0.0
        self.n=False
        self.f_j=None
        self.t_w=None
        self.c_t=tk.Label(R,text="",font=("Helvetica",24),fg="white",bg=BG)
        self.c_t.pack(pady=10)
        self.T=tk.Label(R,text="00:00:00",font=("Helvetica",48),fg="black",bg="yellow")
        self.T.pack(pady=10)
        self.B=tk.Frame(R,bg=BG)
        self.B.pack(pady=10)
        # takefocus=False: 버튼에 포커스가 있으면 Space가 버튼과 단축키에서 두 번 처리됨
        self.s_b=tk.Button(self.B,text="Start",command=self.st,takefocus=False)
        self.s_b.pack(side="left",padx=5)
        self.sT_b=tk.Button(self.B,text="Stop",command=self.sp,takefocus=False)
        self.sT_b.pack(side="left",padx=5)
        self.r_b=tk.Button(self.B,text="Reset",command=self.rs,takefocus=False)
        self.r_b.pack(side="left",padx=5)
        self.td_b=tk.Button(self.B,text="ToDo_list",command=self.otd,takefocus=False)
        self.td_b.pack(side="left",padx=5)
        R.bind("<Key-space>",lambda e:self.tg())
        R.bind("<Key-r>",lambda e:self.rs())
        R.bind("<Key-R>",lambda e:self.rs())
        self.ub()
        self.rt()
    def el(self):
        if self.n:
            return self.t_f+time.monotonic()-self.s_t
        return self.t_f
    def st(self):
        if not self.n:
            self.s_t=time.monotonic()
            self.n=True
            self.ub()
            self.flow()
    def sp(self):
        if self.n:
            self.t_f=self.el()
            self.n=False
            self.cf()
            self.ub()
            self.sh()
    def tg(self):
        if self.n:
            self.sp()
        else:
            self.st()
    def rs(self):
        self.s_t=None
        self.t_f=0.0
        self.n=False
        self.cf()
        self.ub()
        self.sh()
    def flow(self):
        self.sh()
        self.f_j=self.R.after(50,self.flow)
    def cf(self):
        if self.f_j is not None:
            self.R.after_cancel(self.f_j)
            self.f_j=None
    def sh(self):
        fs=int(self.el())
        h,r=divmod(fs,3600)
        m,s=divmod(r,60)
        self.T.config(text=f"{h:02}:{m:02}:{s:02}")
    def ub(self):
        self.s_b.config(state="disabled" if self.n else "normal")
        self.sT_b.config(state="normal" if self.n else "disabled")
    def rt(self):
        n_w=datetime.now()
        self.c_t.config(text=n_w.strftime("%H:%M:%S"))
        # 고정 1000ms 대신 다음 초 경계에 맞춰 예약해서 오차가 쌓이지 않게 함
        self.R.after(1000-n_w.microsecond//1000,self.rt)
    def otd(self):
        if self.t_w is not None and self.t_w.winfo_exists():
            self.t_w.deiconify()
            self.t_w.lift()
            self.t_w.focus_force()
            return
        self.t_w=tk.Toplevel(self.R)
        ToDoListApp(self.t_w)
if __name__=="__main__":
    R=tk.Tk()
    stopwatch=Stopwatch(R)
    R.mainloop()
