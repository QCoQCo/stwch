import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self,R):
        self.R=R
        self.R.title("Stopwatch")
        R.geometry("1200x720")
        self.s_t=None
        self.t_f=timedelta(0)
        self.n=False
        self.c_t=tk.Label(R,text="",font=("Helvetica",24),fg="white")
        self.c_t.pack(pady=10)
        self.T=tk.Label(R,text="00:00:00",font=("Helvetica",48),fg="black",bg="yellow")
        self.T.pack(pady=10)
        self.B=tk.Frame(R)
        self.B.pack(pady=10)
        self.s_b=tk.Button(self.B,text="Start",command=self.st)
        self.s_b.pack(side="left",padx=5)
        self.sT_b=tk.Button(self.B,text="Stop",command=self.sp)
        self.sT_b.pack(side="left",padx=5)
        self.r_b=tk.Button(self.B,text="Reset",command=self.rs)
        self.r_b.pack(side="left",padx=5)
        self.flow()
        self.rt()
    def st(self):
        if not self.n:
            self.s_t=datetime.now()-self.t_f
            self.n=True
    def sp(self):
        if self.n:
            self.t_f=datetime.now()-self.s_t
            self.n = False
    def rs(self):
        self.s_t=None
        self.t_f=timedelta(0)
        self.n=False
        self.T.config(text="00:00:00")
    def flow(self):
        if self.n:
            self.t_f=datetime.now()-self.s_t
            fs=int(self.t_f.total_seconds())
            h,r=divmod(fs,3600)
            m,s=divmod(r,60)
            self.T.config(text=f"{h:02}:{m:02}:{s:02}")
        self.R.after(50,self.flow)
    def rt(self):
        r_t=datetime.now().strftime("%H:%M:%S")
        self.c_t.config(text=r_t)
        self.R.after(1000,self.rt)
if __name__=="__main__":
    R=tk.Tk()
    R.configure(bg='black')
    stopwatch=Stopwatch(R)
    R.mainloop()