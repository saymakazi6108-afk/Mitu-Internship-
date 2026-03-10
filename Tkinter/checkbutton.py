import tkinter as tk 

wd = tk.Tk()

wd.title("check button")
wd.geometry("300x300")

var = tk.IntVar() # store checkbox status 

def check_status():
        #var.get() - read value 
    if var.get() == 1: 
        # 1: checked 0: unchecked
        label.config(text="you agreed ...")
    else:
        label.config(text="you did not agree...")

cb = tk.Checkbutton(

    wd,
    text="i agree",
    variable=var, # connect checkbox to variable 
    command=check_status
)
cb.pack(pady=10)

label = tk.Label(wd, text="please select checkbox ")
label.pack()

wd.mainloop()
