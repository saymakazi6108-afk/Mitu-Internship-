student = [] # list that used to store student data

#display menu to the user
def show_menu(): 
    print("----------Student Management Tracker----------")
    print("Enter you choice : ")
    print("1. Add student")
    print("2. View student")
    print("3.Exit")

#Adding student data
def add_std():
    name = input("Enter you name : ")
    age = input("Enter you age : ")

    student.append({"name" : name , "age" : age}) # we created a dictionary inside a list of each student 
    
    print("student info added successfully...")

#Display student data to the user 
def view_std():
    if len(student) == 0 :
        print("Data is not available")

    else:
        print("Name : " + name)
        print("Age : " + age)
        print("-----------")

while True:
    show_menu()

    if 