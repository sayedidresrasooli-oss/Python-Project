import tkinter as tk

window = tk.Tk()
window.title("Mouse Drawing Pad")
window.geometry("500x500")
canvas = tk.Canvas(
    window,
    width = 700,
    height = 400,
    background = "white",
)

canvas.pack(fill = "both", expand = True)

def draw(event):
    r = 3

    ball = canvas.create_oval(
        event.x - r,
        event.y - r,
        event.x + r,
        event.y + r,
        fill = "red",
        outline = "red",
    )
    canvas.move(
        ball,
        10,
        0
    )

    coords = canvas.coords(ball)
    print(coords)



def delete():
    canvas.delete()

button = tk.Button(
    window,
    text="Clear",
    command=delete
    )

button.pack()

canvas.bind("<B1-Motion>", draw)

window.mainloop()