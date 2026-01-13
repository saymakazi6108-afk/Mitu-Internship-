import tkinter as tk 

window = tk.Tk()


window.title("My graphics") # title 
window.geometry("300x400") # size

label = tk.Label(window , text="hello everyone !!") # adding label widget 
label.pack()

window.mainloop()
