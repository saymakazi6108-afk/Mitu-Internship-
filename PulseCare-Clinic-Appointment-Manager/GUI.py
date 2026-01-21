import tkinter as tk
from tkinter import ttk, messagebox
import csv
from patient_add import Patient
from doctor import doc

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("PulseCare - Clinic Appointment Manager")
root.geometry("900x700")
root.config(bg="#F4F6F6")

# ---------------- HEADER ----------------
tk.Label(
    root,
    text="PulseCare - Clinic Appointment Manager",
    font=("Arial", 18, "bold"),
    fg="#013434",
    bg="#03D7D7",
    pady=10
).pack(fill="x")

# ---------------- MAIN FRAME ----------------
main_frame = tk.Frame(root, bg="#F4F6F6")
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

left_frame = tk.Frame(main_frame, bg="#F4F6F6")
left_frame.grid(row=0, column=0, padx=20, sticky="n")

right_frame = tk.Frame(main_frame, bg="#F4F6F6")
right_frame.grid(row=0, column=1, padx=20, sticky="n")

# ---------------- FORM ----------------
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

tk.Label(left_frame, text="Patient Name", bg="#F4F6F6").grid(row=1, column=0, sticky="w")
patient_entry = tk.Entry(left_frame, width=25)
patient_entry.grid(row=1, column=1, pady=5)

tk.Label(left_frame, text="Age", bg="#F4F6F6").grid(row=2, column=0, sticky="w")
age_entry = tk.Entry(left_frame, width=25)
age_entry.grid(row=2, column=1, pady=5)

emergency_var = tk.IntVar()
tk.Checkbutton(
    left_frame,
    text="Emergency Case",
    variable=emergency_var,
    bg="#F4F6F6"
).grid(row=3, column=1, sticky="w")

# ---------------- LISTBOXES ----------------
tk.Label(right_frame, text="Waiting Patients", font=("Arial", 13, "bold"),
         fg="#0D47A1", bg="#F4F6F6").pack(anchor="w")

waiting_list = tk.Listbox(right_frame, width=45, height=10)
waiting_list.pack()

tk.Label(right_frame, text="Completed Patients", font=("Arial", 13, "bold"),
         fg="#1B5E20", bg="#F4F6F6").pack(anchor="w", pady=(10, 0))

completed_list = tk.Listbox(right_frame, width=45, height=10)
completed_list.pack()

# ---------------- FUNCTIONS ----------------
def refresh_waiting():
    waiting_list.delete(0, tk.END)

    for doctor, queue in doc.items():
        for p in queue:
            index = waiting_list.size()

            waiting_list.insert(
                tk.END, f"{p.name} | {doctor} | Waiting"
            )

            
            if p.emergency == 1:
                waiting_list.itemconfig(index, fg="red")


def add_patient():
    name = patient_entry.get().strip()
    age = age_entry.get().strip()

    if not name or not age.isdigit():
        messagebox.showerror("Error", "Enter valid name and age")
        return

    patient = Patient(name, age, emergency_var.get())
    queue = doc[doctor_var.get()]

    if patient.emergency:
        queue.insert(0, patient)
    else:
        queue.append(patient)

    refresh_waiting()
    patient_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def next_patient():
    queue = doc[doctor_var.get()]
    if not queue:
        messagebox.showinfo("Info", "No patients waiting")
        return

    patient = queue.pop(0)
    completed_list.insert(
        tk.END, f"{patient.name} | {doctor_var.get()} | Completed"
    )

    with open("patient_history.csv", "a", newline="") as file:
        csv.writer(file).writerow(
            [patient.name, patient.age, doctor_var.get()]
        )

    refresh_waiting()

def open_patient_history():
    win = tk.Toplevel(root)
    win.title("Patient History")
    win.geometry("600x400")

    tree = ttk.Treeview(win, columns=("name", "age", "doctor"), show="headings")
    tree.heading("name", text="Name")
    tree.heading("age", text="Age")
    tree.heading("doctor", text="Doctor")

    tree.pack(fill="both", expand=True)

    try:
        with open("patient_history.csv") as f:
            for row in csv.reader(f):
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        pass

# ---------------- BUTTONS ----------------
tk.Button(left_frame, text="Add Patient", command=add_patient,
          bg="#2E7D32", fg="white", width=18).grid(row=4, column=1, pady=10)

tk.Button(left_frame, text="Next Patient", command=next_patient,
          bg="#0288D1", fg="white", width=18).grid(row=5, column=1)

tk.Button(left_frame, text="Patient History", command=open_patient_history,
          bg="#6A1B9A", fg="white", width=18).grid(row=6, column=1, pady=10)

# ---------------- RUN ----------------
root.mainloop()
