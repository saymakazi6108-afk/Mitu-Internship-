import tkinter as tk

window = tk.Tk()

window.geometry("300x300")

frame = tk.Frame(window)
frame.pack()

tk.Label(frame, text="Inside Frame").pack()

window.mainloop()