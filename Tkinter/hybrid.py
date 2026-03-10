class A :
    def show1(self):
        print("class A")

class B(A) : 
    def show2(self) :
        print("class B")

class C(A) :
    def show3(self) :
        print("class C")

class D(B,C):
    def show4(self):
        print("class D")

d1 = D()
d1.show1()
d1.show2()
d1.show3()
d1.show4()
