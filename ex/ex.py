'''import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            print("Stopwatch started.")

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            print(f"Stopwatch stopped at {self.elapsed_time:.2f} seconds.")

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        print("Stopwatch reset.")

    def get_elapsed_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time

def main():
    stopwatch = Stopwatch()
    while True:
        command = input("Enter command (start/stop/reset/exit): ").strip().lower()
        if command == 'start':
            stopwatch.start()
        elif command == 'stop':
            stopwatch.stop()
        elif command == 'reset':
            stopwatch.reset()
        elif command == 'exit':
            break
        else:
            print("Invalid command. Please enter 'start', 'stop', 'reset', or 'exit'.")

if __name__ == "__main__":
    main()
'''
'''
from datetime import datetime
e_time=0
E=datetime.__new__
E2=datetime.now()
print(E)
print(E2)
'''
import tkinter as tk

# 메인 윈도우 생성
root = tk.Tk()
root.title("Tkinter Label 예제")
root.geometry("300x200")

# 레이블 생성
label = tk.Label(root, text="안녕하세요, Tkinter!", font=("Arial", 16), fg="blue", bg="yellow")
label.pack(pady=20)

# 메인 루프 실행
root.mainloop()