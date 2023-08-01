import time
import tkinter as tk

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("专注时钟")
root.geometry("200x100")

clock_label = tk.Label(root, font=("Arial", 30))
clock_label.pack()

update_clock()

root.mainloop()
