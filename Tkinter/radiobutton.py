import tkinter as tk

wd = tk.Tk()

wd.geometry("300x300")

v = tk.IntVar()

tk.Radiobutton(wd,text="C++",variable=v,value=1).pack()
tk.Radiobutton(wd,text="java",variable=v,value=2).pack()
tk.Radiobutton(wd,text="python",variable=v,value=3).pack()

wd.mainloop()