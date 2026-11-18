import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
window.title('Keyboard event viewer')

label = tk.Label(
    window,
    text='keyboard event viewer',
    font=('Arial', 20)
)
label.pack(pady=20)


entry = tk.Entry(
    window,
    width=50,
    highlightcolor="blue",
    highlightthickness=1,
)
entry.pack()

status = tk.Label(
    window,
    text='Waiting...',
)
status.pack(pady=10)

def click(event):
    print(event.keysym)
    print(event.char)

window.bind("<KeyPress>", click)
window.bind("<Escape>", click)

def gained_focus(event):
    status.config(text='Gained focus')

def lose_focus(event):
    status.config(text='Lose focus')

entry.bind("<FocusIn>", gained_focus)
entry.bind("<FocusOut>", lose_focus)

window.mainloop()