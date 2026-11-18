import time
import tkinter as tk

window = tk.Tk()
window.title("Keyboard Controlled Player")
window.geometry("500x500")

canvas = tk.Canvas(window, width = 500, height = 500,background = "green")
canvas.pack()

oval = canvas.create_oval(50,50,150,150,fill="red")

coords = canvas.coords(oval)
print(coords)

def move_player(event):
    moves = {
        "Left": (-10, 0),
        "Right": (10, 0),
        "Up": (0, -10),
        "Down": (0, 10),
    }

    if event.keysym in moves:
        dx, dy = moves[event.keysym]
        canvas.move(oval, dx, dy)

window.bind("<KeyPress>", move_player)

def animate():
    canvas.move(
        oval,
        5,
        0
    )

    window.after(100, animate)

animate()

def delete_show():
    canvas.delete(oval)
    window.after(100, delete_show)

button = tk.Button(window, text = "Delete", command = delete_show)
button.pack()

window.mainloop()

