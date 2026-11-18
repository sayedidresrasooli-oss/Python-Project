import tkinter as tk



window = tk.Tk()
window.geometry("500x500")
window.title("Bouncing Ball")

canvas = tk.Canvas(window, width=500, height=500, bg="green")
canvas.pack(fill="both", expand=True)
ball = canvas.create_oval(
    220,50,320,150
)

def animate():
    canvas.move(
        ball,
        10,
        0
    )

    window.after(1000, animate)

animate()

coords = canvas.coords(ball)
print(coords)


window.mainloop()
