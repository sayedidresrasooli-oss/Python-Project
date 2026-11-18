import tkinter as tk


root = tk.Tk()
root.geometry("500x500")
root.configure(
    bg="#0E0A2B"
)

title = root.title("Student Management System")
title2 = tk.Label(
    root,
    text = "Student Management System",
    font = ("Arial Bold", 20),
    bg = "#0E0A2B",
    fg = "white"
)
title2.pack(pady = 20, side = "top")
name_entry = tk.Entry(
    root,
    width = 40
)
name_entry.pack(pady = 20, padx = 100)
name = name_entry.get()
name_entry.insert(0,"Name")

id_entry = tk.Entry(
    root,
    width = 40
)
id_entry.pack(pady = 20)
id_entry.insert(0,"ID")

email_entry = tk.Entry(
    root,
    width = 40
)
email_entry.pack(pady = 20)
email_entry.insert(0,"Email")

phone_entry = tk.Entry(
    root,
    width = 40
)
phone_entry.pack(pady = 20)
phone_entry.insert(0,"Phone")

address = tk.Text(
    root,
    width = 30,
    height = 3,
    wrap = "word"
)

address.pack(pady = 20)

address.insert("1.0","Enter your  address")

root.mainloop()






