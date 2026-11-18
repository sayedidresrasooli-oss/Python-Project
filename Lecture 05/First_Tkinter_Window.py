import tkinter as tk
import webbrowser


def open_browser():
    webbrowser.open("https://github.com/sayedidresrasooli-oss/Python-Project")

window = tk.Tk()
window.geometry("500x500")
window.title("Advanced Programming Lab")
window.configure(bg = "#8250DF")
label = tk.Label(
    window,
    text = "GitHub Log in Page",
    bg = "#8250DF",
    fg = "white",
    font = ("Arial bold", 20)
)
label.pack()

name = tk.Entry(
    window,
    width = 35
)

name.insert(tk.END, "name")

name.pack(pady = 20)

email = tk.Entry(
    window,
    width = 35
)

email.insert(tk.END, "email")
email.pack(pady = 20)

password = tk.Entry(
    window,
    width = 35
)
password.insert(tk.END, "password")
password.pack(pady = 20)

button1 = tk.Button(
    window,
    text = "Login",
    command = open_browser
)
button1.pack(pady = 10)

button2 = tk.Button(
    window,
    text = "Sign up"
)

button2.pack(pady = 10)

button3 = tk.Button(
    window,
    text = "log out"
)

button3.pack(pady = 10)

window.mainloop()