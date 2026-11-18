import tkinter as tk

window = tk.Tk()
window.geometry('500x500')

label = tk.Label(
    window,
    text="Login Page",
    font=("Arial bold", 25),
    fg="green"
)

label.pack(pady=40)


user = tk.Label(
    window,
    text="Username :",
    font=("Arial bold", 10),
)
user.pack(pady=0)

username = tk.Entry(
    window,
    width=50,
    highlightbackground='black',
    highlightcolor='blue',
    highlightthickness=1,
)
username.pack(pady=40)

passw = tk.Label(
    window,
    text="Password : ",
    font=("Arial bold", 10),
)

passw.pack(pady=0)

password = tk.Entry(
    window,
    width=50,
    highlightbackground='black',
    highlightcolor='blue',
    highlightthickness=1,
)

password.pack(pady=20)

def login():
    print("You are login")

button = tk.Button(
    window,
    text="Login",
    command= login,
    fg="green",
)

button.pack(pady=10,padx=10)




def submit(event = None):
    name = username.get().strip()
    print(f"name : {name}")

username.bind("<Return>", submit)

status = tk.Label(
    window,
    text="Waiting..."
)

status.pack()

def gained_focus(event):
    status.config(text="Input active")

def lose_focus(event):
    status.config(text="Input left")

username.bind("<FocusIn>", gained_focus)
username.bind("<FocusOut>", lose_focus)
password.bind("<FocusIn>", gained_focus)
password.bind("<FocusOut>", lose_focus)


window.mainloop()