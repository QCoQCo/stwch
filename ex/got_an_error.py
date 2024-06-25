import tkinter as tk
from datetime import datetime

class Stopwatch:

    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.start_time = None
        self.elapsed_time =0
        self.running = False

        self.time_label = tk.Label(root, text="0.00", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="right")

        self.update_time()

    def start(self):
        if not self.running:
            '''
            if self.elapsed_time == 0:
                self.start_time = datetime.now()
            else:
                self.start_time = datetime.now() - self.elapsed_time
            '''
            self.start_time = datetime.now() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.time_label.config(text="0.00")

    def update_time(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            elapsed_seconds = self.elapsed_time.total_seconds()
            self.time_label.config(text=f"{elapsed_seconds:.2f}")
        self.root.after(50, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()