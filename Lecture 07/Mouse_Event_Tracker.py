import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("Mouse Tracker")


position_label = tk.Label(
    window,
    text="Move your mouse",
    font=("Arial", 12),
    bg="white",
)

position_label.pack()

def click(event):
    position_label.config(
        text=f"x= {event.x},y= {event.y}"
    )


window.bind("<Motion>", click)

def left_click(event):
    print("left click")

window.bind("<Button-1>", left_click)

def double_click(event):
    print("double click")

window.bind("<Double-Button-1>", double_click)

def enter(event):
    print("enter")

window.bind("<Enter>", enter)
window.mainloop()