import tkinter as tk
from tkinter import messagebox

w = tk.Tk()
w.title("MessageBox Example")
        
w.geometry("300x400")

def show_message():
    messagebox.showinfo("Info", "Hello User")

def warning():
    messagebox.showwarning("Warning", "This is a warning")

def error():
    messagebox.showerror("Error", "Something went wrong")

def ask():
    result = messagebox.askyesno("Confirm", "Do you want to continue?")
    if result:
        messagebox.showinfo("Result", "You clicked YES")
    else:
        messagebox.showinfo("Result", "You clicked NO")

tk.Button(w, text="Show Message", command=show_message).pack(pady=10)
tk.Button(w, text="Show Warning", command=warning).pack(pady=10)
tk.Button(w, text="Show Error", command=error).pack(pady=10)
tk.Button(w, text="Show Permission", command=ask).pack(pady=10)

w.mainloop()
