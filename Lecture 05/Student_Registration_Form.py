import tkinter as tk
import webbrowser
from builtins import id


def save():

    value1 = id.get()
    value2 = name.get()
    value3 = department.get()
    value4 = semester.get()
    print(value1)
    print(value2)
    print(value3)
    print(value4)

def clear():
    id.delete(0, "end")
    name.delete(0, "end")
    department.delete(0, "end")
    semester.delete(0, "end")


window = tk.Tk()
window.title("Student Registration Form")
window.geometry("500x500")
form = tk.Frame(
    window,
    pady = 20,
    padx = 20,
    bg = "light blue"
)
form.pack(fill = "both", expand = "True")

label = tk.Label(
    form,
    text = "Student Registration Form",
    font = ("Arial bold", 20),
    bg = "light blue"
)
label.grid(row = 0, column = 0,pady = 20, sticky = "e")

id = tk.Entry(
    form,
    width = 50
)
id.insert(tk.END, "Student ID")

id.grid(row = 2, column = 0, pady = 10, padx=20, sticky="w")

name = tk.Entry(
    form,
    width = 50
)

name.insert(tk.END, "Student Name")

name.grid(row = 3, column = 0, pady = 10, padx=20, sticky="w")

department = tk.Entry(
    form,
    width = 50
)
department.insert(tk.END, "Department")

department.grid(row = 4, column = 0, pady = 10, padx=20, sticky="w")

semester = tk.Entry(
    form,
    width = 50
)

semester.insert(tk.END, "Semester")

semester.grid(row = 5, column = 0, pady = 10, padx=20, sticky="w")

button1 = tk.Button(
    form,
    text = "submit",
    command = save
)

button1.grid(row = 6, column = 0, pady = 10, padx = 33, sticky="e")

button2 = tk.Button(
    form,
    text = "cancel",
    command = clear
)

button2.grid(row = 6, column = 0, pady = 20, padx=20, sticky="w")

label1 = tk.Label(
    form,
    text = "Continue with google",
    font = ("Arial bold", 10, "underline"),
    bg = "light blue",
    fg = "black"
)

label1.grid(row = 7, column = 0, pady = 20, padx=20, sticky="n")
label1.bind("<Button -1>", lambda e: webbrowser.open("www.google.com"))

label2 = tk.Label(
    form,
    text = "Continue with GitHub",
    font = ("Arial bold", 10, "underline"),
    bg = "light blue",
    fg = "black"
)

label2.grid(row = 8, column = 0, pady = 20, padx=20, sticky="n")

label2.bind("<Button -1>", lambda e: webbrowser.open("www.github.com"))

label3 = tk.Label(
    form,
    text = "Continue with LinkedIn",
    font = ("Arial bold", 10, "underline"),
    bg = "light blue",
    fg = "black"
)

label3.grid(row = 9, column = 0, pady = 20, padx=20, sticky="n")
label3.bind("<Button -1>", lambda e: webbrowser.open("www.linkedin.com"))

window.mainloop()