class A:
    def display(self):
        print("hello !!")

class B(A):
    def display1(self):
        print("I'm Sayma ")

class C(B) :
    def display2(self):
        print("I'm pursuing diploma in IT")

c1 = C()
c1.display()
c1.display1()
c1.display2()

