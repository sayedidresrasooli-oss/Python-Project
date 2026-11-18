import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

label1 = tk.Label(
    window,
    text = "Hacker Rank",
    font = ("Arial bold", 20),
)

label1.grid(row = 0, column = 0, padx = 20, pady = 20)

label2 = tk.Label(
    window,
    text = "Profile Page",
    font = ("Arial bold", 10)
)

label2.grid(row = 1, column = 0, padx = 45, pady = 10, sticky = "w")

label3 = tk.Label(
    window,
    text = "Register Page",
    font = ("Arial bold", 10)
)

label3.grid(row = 2, column = 0, padx = 45, pady = 10, sticky = "w")

window.mainloop()