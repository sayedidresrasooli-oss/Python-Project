import tkinter as tk

window = tk.Tk()
window.title("Image Profile Card")
window.geometry("500x500")

frame = tk.Frame(
    window,
    width=500,
    height=500,
    bg="light blue",
)

frame.pack(side="top", fill="both", expand=True)

label = tk.Label(
    frame,
    text="Image Profile Card",
    font=("Arial", 20, "bold"),
    fg="black",
)

label.grid(row=0, column=0, pady=10, padx=20,sticky="w")

name = tk.Entry(
    frame,
    width=50,
    highlightcolor="blue",
    highlightthickness=2,
)
name.grid(row=1, column=0, pady=20, padx=20)
name.insert(tk.END, "Name")

department = tk.Entry(
    frame,
    width=50,
    highlightcolor="blue",
    highlightthickness=2,
)

department.grid(row=2, column=0, pady=20, padx=20)
department.insert(tk.END, "Department")

email = tk.Entry(
    frame,
    width=50,
    highlightcolor="blue",
    highlightthickness=2,
)

email.grid(row=3, column=0, pady=20, padx=20)
email.insert(tk.END, "Email")

def add():
    name.delete(0, tk.END)
    department.delete(0, tk.END)
    email.delete(0, tk.END)

button = tk.Button(
    frame,
    text="Edit",
    bg="white",
    fg="black",
    command=add,
)

button.grid(row=4, column=0, pady=20,padx=20 ,sticky="e")

def submit_form():
    print(name.get())
    print(department.get())
    print(email.get())

button1 = tk.Button(
    frame,
    text="Submit",
    command=submit_form,
)

button1.grid(row=4, column=0, pady=20, padx=20, sticky="w")



window.mainloop()