import tkinter as tk
window = tk.Tk()

window.title("Entery")
window.geometry("300x300")

def show_text():
    label2.config(text="form submitted successfully...")


label = tk.Label(window, text="hello GPP student")
label.pack()

label1 = tk.Label(window, text="Enter your name")
label1.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="submit", command= show_text)
button.pack()

label2 = tk.Label(window , text=" ")
label2.pack()

window.mainloop()