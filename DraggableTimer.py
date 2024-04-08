import tkinter as tk
import time

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

def zoom(event):
    global current_font_size
    if event.state & 0x4:  
        zoom_direction = event.delta
        if event.delta == 0:
            zoom_direction = event.num - 2
        increment = 1 if zoom_direction > 0 else -1  
        
        new_size = current_font_size + increment
        if new_size < 10: 
            new_size = 10
        current_font_size = new_size 
        
        label.config(font=("Calibri", current_font_size))

root = tk.Tk()
root.title("Clock")
root.configure(bg="black")

current_font_size = 200  

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

label = tk.Label(root, text="", font=("Calibri", current_font_size), fg="white", bg="black", cursor="hand2")
label.place(x=screen_width//4, y=screen_height//4)

update_time()

label.bind("<ButtonPress-1>", on_drag_start)
label.bind("<B1-Motion>", on_drag_motion)
label.bind("<MouseWheel>", zoom)

root.mainloop()
