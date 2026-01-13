import tkinter as tk

def login():
    print("User:", user.get())
    print("Pass:", pwd.get())

window = tk.Tk()
window.title("Login")

tk.Label(window, text="Username").grid(row=0, column=0)
user = tk.Entry(window)
user.grid(row=0, column=1)

tk.Label(window, text="Password").grid(row=1, column=0)
pwd = tk.Entry(window, show="*")
pwd.grid(row=1, column=1)

tk.Button(window, text="Login", command=login).grid(row=2, column=1)

window.mainloop()
