import tkinter as tk

wd = tk.Tk()

wd.title("see")
wd.geometry("300x300")

tk.Label(wd, text="enter your name : ").grid(row= 0 , column= 0)
tk.Entry(wd).grid(row=0 , column=1)

tk.Label(wd, text="enter your age : ").grid(row=1,column=0)
tk.Entry(wd).grid(row=1,column=1)


wd.mainloop()