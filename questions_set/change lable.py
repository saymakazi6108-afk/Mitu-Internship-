import tkinter as tk

window = tk.Tk()

window.title("change label")
window.geometry("300x300")

def click_me():
    label.config(text="after clicking button")

label = tk.Label(window, text="before button clicking")
label.pack()

button = tk.Button(window, text="click me", command=click_me)
button.pack()

window.mainloop()