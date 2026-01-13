import tkinter as tk

window = tk.Tk()

window.title("see this")
window.geometry("300x300")

def show2():
    print(entry.get())

l1 = tk.Label(window, text= "welcome to programming")
l1.pack()

l2 = tk.Label(window, text="Enter your age")
l2.pack()

entry = tk.Entry(window)
entry.pack()

btn = tk.Button(window, text="Submit", command=show2)
btn.pack()

window.mainloop()