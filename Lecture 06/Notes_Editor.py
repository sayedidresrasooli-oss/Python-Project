import tkinter as tk

window = tk.Tk()
window.title("Notes Editor")
window.geometry("500x500")

label = tk.Label(
    window,
    text="Notes Editor",
    font=("Arial bold", 20),
    fg="black",
    bg="white",
)

label.pack(side="top", pady=20)
text = tk.Text(
    window,
    height=10,
    width=40,
)
text.pack(expand=True)
text.insert(tk.END, "Enter your notes here")

button1 = tk.Button(
    window,
    text="Clear",
    command=lambda: text.delete("1.0", tk.END),
)
button1.pack()

def disable_button(status):
    status.config(state=tk.DISABLED)

button2 = tk.Button(
    window,
    text="Disable",
    command=disable_button
)
button2.pack()
window.mainloop()