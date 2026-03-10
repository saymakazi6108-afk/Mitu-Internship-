import tkinter as tk 

window = tk.Tk()

window.title("Sayma")
window.geometry("200x200")

def click_me():
    print("Button clicked")
    
btn = tk.Button(window, text ="Click me")
btn.pack()

btn1 = tk.Button(window, text="here", command=click_me)
btn1.pack()

window.mainloop()

