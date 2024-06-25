import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        root.geometry("1200x720")
        self.start_time = None
        self.elapsed_time = timedelta(0)
        self.running = False

        # 현재 시간 라벨을 상단에 배치 (글자색: 흰색)
        self.current_time_label = tk.Label(root, text="", font=("Helvetica", 24), fg="white")
        self.current_time_label.pack(pady=10)

        # 경과 시간 라벨을 중앙에 배치 (글자색: 흰색)
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), fg="black", bg="yellow")
        self.time_label.pack(pady=10)

        # 버튼들을 하단에 배치
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start)
        self.start_button.pack(side="left", padx=5)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", padx=5)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=5)

        self.update_time()
        self.update_current_time()

    def start(self):
        if not self.running:
            self.start_time = datetime.now() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = None
        self.elapsed_time = timedelta(0)
        self.running = False
        self.time_label.config(text="00:00:00")

    def update_time(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            elapsed_seconds = int(self.elapsed_time.total_seconds())
            hours, remainder = divmod(elapsed_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.root.after(50, self.update_time)

    def update_current_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=current_time)
        self.root.after(1000, self.update_current_time)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='black')  # 배경 색상을 검은색으로 설정
    stopwatch = Stopwatch(root)
    root.mainloop()