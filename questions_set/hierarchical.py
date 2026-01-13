class person:
    def show1(self):
        print("this class is for person")

class student(person):
    def show2(self):
        print("this class for students")

class teacher(person):
    def show3(self):
        print("this class for teachers")

s1 = student()
s1.show1()
s1.show2()

t1 = teacher()
t1.show1()
t1.show3()