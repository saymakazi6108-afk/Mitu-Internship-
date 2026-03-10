import tkinter as tk
from tkinter import ttk 
from patient_add import Patient
from doctor import doc

# creating main window 
root = tk.Tk()

root.title("PulseCare - Clinic Appoinment Manager")
root.geometry("900x700")
root.config(bg="#F4F6F6")

# Creating header 
header = tk.Label(
    root,
    text="PulseCare - Clinic Appoinment Manager",
    font=("Arial",18,"bold"),
    fg="#013434",
    bg="#03D7D7",
    pady=10
)
header.pack(fill="x")

# Creating doctor lists 

doctors = tk.Label(
    root,
    text="Select Doctor : ",
    bg="#F4F6F6"
)
doctors.place(x=50,y=80)

doctor_var = tk.StringVar()

doctor_combo = ttk.Combobox(
    root,
    textvariable=doctor_var,
    values=list(doc.keys()),
    state="readonly"
)

doctor_combo.place(x=170,y=80)
doctor_combo.current(0)

# Patient input 

patient_name = tk.Label(root,text="Patient Name : ").place(x=50, y=130)

patinet_entry = tk.Entry(root)
patinet_entry.place(x=170, y=130)

age = tk.Label(root,text="Age : ").place(x=50, y=170)

age_entry = tk.Entry(root)
age_entry.place(x=170, y=170)

emergency_var = tk.IntVar()
emergency = tk.Checkbutton(
    root ,
    text="Emergency",
    variable=emergency_var,
    bg="#F4F6F6"
).place(x=170, y=210)

# Adding patient 

def add_patient() :
    name = patinet_entry.get()
    age = age_entry.get()
    emergency = emergency_var.get()

    new_patient = Patient(name, age, emergency)
    queue = doc[doctor_var.get()]

    if emergency :
        queue.insert(0,new_patient)
    else:
        queue.append(new_patient)

    replace_list()
    
tk.Button(
    root,
    text="Add Patient",
    command=add_patient,
    bg="#2E7D32",     # green
    fg="white",
    font=("Arial", 11, "bold")
).place(x=600, y=80)

# display list 

patient_list = tk.Listbox(root, width = 60 , height = 15)
patient_list.place(x=400, y=100)

def replace_list():
    patient_list.delete(0,tk.END)

    for p in doc[doctor_var.get()]:
        if emergency :
            patient_list.insert(tk.END , f"{p.name} (Emergency)")
            patient_list.itemconfig(tk.END , fg="red")
        else:
            patient_list.insert(tk.END, f"{p.name} - Waiting")


def next_patient():
    queue = doc[doctor_var.get()]

    if queue: 
        patient = queue.pop(0)
        patient.status("completed")
        replace_list()

    
tk.Button(
    root,
    text="Next Patient",
    command=next_patient,
    bg="#0288D1",
    fg="white"
).place(x=170, y=260)

root.mainloop()


import tkinter as tk
from tkinter import ttk
import csv
from patient_add import Patient
from doctor import doc


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("PulseCare - Clinic Appointment Manager")
root.geometry("900x700")
root.config(bg="#F4F6F6")

# ---------------- HEADER ----------------
header = tk.Label(
    root,
    text="PulseCare - Clinic Appointment Manager",
    font=("Arial", 18, "bold"),
    fg="#013434",
    bg="#03D7D7",
    pady=10
)
header.pack(fill="x")

# ---------------- MAIN FRAME ----------------
main_frame = tk.Frame(root, bg="#F4F6F6")
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# ---------------- LEFT FRAME (FORM) ----------------
left_frame = tk.Frame(main_frame, bg="#F4F6F6")
left_frame.grid(row=0, column=0, sticky="nw", padx=20)

# Doctor
tk.Label(left_frame, text="Select Doctor", bg="#F4F6F6").grid(row=0, column=0, sticky="w")
doctor_var = tk.StringVar()
doctor_combo = ttk.Combobox(
    left_frame,
    textvariable=doctor_var,
    values=list(doc.keys()),
    state="readonly",
    width=22
)
doctor_combo.grid(row=0, column=1, pady=5)
doctor_combo.current(0)

# Patient Name
tk.Label(left_frame, text="Patient Name", bg="#F4F6F6").grid(row=1, column=0, sticky="w")
patient_entry = tk.Entry(left_frame, width=25)
patient_entry.grid(row=1, column=1, pady=5)

# Age
tk.Label(left_frame, text="Age", bg="#F4F6F6").grid(row=2, column=0, sticky="w")
age_entry = tk.Entry(left_frame, width=25)
age_entry.grid(row=2, column=1, pady=5)

# Emergency
emergency_var = tk.IntVar()
tk.Checkbutton(
    left_frame,
    text="Emergency Case",
    variable=emergency_var,
    bg="#F4F6F6"
).grid(row=3, column=1, sticky="w", pady=5)

# ---------------- FUNCTIONS ----------------
def open_patient_history():
    history_win = tk.Toplevel(root)
    history_win.title("Patient History")
    history_win.geometry("600x400")

    columns = ("name", "age", "doctor")

    tree = ttk.Treeview(
        history_win,
        columns=columns,
        show="headings"
    )

    tree.heading("name", text="Patient Name")
    tree.heading("age", text="Age")
    tree.heading("doctor", text="Doctor Name")

    tree.column("name", width=200)
    tree.column("age", width=80)
    tree.column("doctor", width=180)

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    try:
        with open("patient_history.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        pass

def save_patient_history(name, age, doctor):
    with open("patient_history.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, doctor])

def replace_list():
    waiting_list.delete(0, tk.END)
    completed_list.delete(0, tk.END)

    for doctor, queue in doc.items():
        for p in queue:
            waiting_list.insert(
                tk.END,
                f"{p.name} | {doctor} | Waiting"
            )



def add_patient():
    name = patient_entry.get()
    age = age_entry.get()
    emergency = emergency_var.get()

    

    new_patient = Patient(name, age, emergency)
    new_patient.status = "Waiting"
    queue = doc[doctor_var.get()]

    if emergency:
        queue.insert(0, new_patient)
    else:
        queue.append(new_patient)

    replace_list()

def next_patient():
    queue = doc[doctor_var.get()]
    if queue:
        patient = queue.pop(0)
        patient.status = "Completed"

        completed_list.append(
            f"{patient.name} | {doctor_var.get()} | Completed"
        )

        save_patient_history(
            patient.name,
            patient.age,
            doctor_var.get()
        )

        replace_list()

        completed_list.delete(0, tk.END)
        for p in completed_list:
            completed_list.insert(tk.END, p)




# ---------------- BUTTONS ----------------
tk.Button(
    left_frame,
    text="Add Patient",
    command=add_patient,
    bg="#2E7D32",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
).grid(row=4, column=1, pady=10)

tk.Button(
    left_frame,
    text="Next Patient",
    command=next_patient,
    bg="#0288D1",
    fg="white",
    width=18
).grid(row=5, column=1, pady=5)

tk.Button(
    left_frame,
    text="Patient History",
    command=open_patient_history,
    bg="#6A1B9A",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
).grid(row=6, column=1, pady=10)

# ---------------- RIGHT FRAME (LISTS) ----------------
right_frame = tk.Frame(main_frame, bg="#F4F6F6")
right_frame.grid(row=0, column=1, padx=20, sticky="n")

# WAITING PATIENTS
tk.Label(
    right_frame,
    text="Waiting Patients",
    font=("Arial", 13, "bold"),
    fg="#0D47A1",
    bg="#F4F6F6"
).pack(anchor="w")

waiting_list = tk.Listbox(right_frame, width=45, height=8)
waiting_list.pack(pady=5)

# COMPLETED PATIENTS
tk.Label(
    right_frame,
    text="Completed Patients",
    font=("Arial", 13, "bold"),
    fg="#1B5E20",
    bg="#F4F6F6"
).pack(anchor="w", pady=(10, 0))

completed_list = tk.Listbox(right_frame, width=45, height=8)
completed_list.pack(pady=5)



# ---------------- RUN ----------------
root.mainloop()
