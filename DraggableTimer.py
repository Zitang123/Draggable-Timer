import tkinter as tk
import time


start_x = 0
start_y = 0

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

def on_drag_start(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def on_drag_motion(event):
    x = label.winfo_x() + (event.x - start_x)
    y = label.winfo_y() + (event.y - start_y)
    label.place(x=x, y=y)

root = tk.Tk()
root.title("Clock")
root.configure(bg="black")  


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


label = tk.Label(root, text="", font=("Calibri", 200), fg="white", bg="black", cursor="hand2")
label.place(x=screen_width//4, y=screen_height//4) 

update_time()


label.bind("<ButtonPress-1>", on_drag_start)
label.bind("<B1-Motion>", on_drag_motion)

root.mainloop()
