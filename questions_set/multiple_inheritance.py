class A :
    def show1(self): 
        print("It is first parent class ")

class B() : 
    def show2(self):
        print("It is second parent class")

class C() :
    def show3(self) :
        print("It is third parent class")

class D(A,B,C):
    def show4(self):
        print("IT is child class")

d1 = D()
d1.show1()
d1.show2()
d1.show3()
d1.show4()