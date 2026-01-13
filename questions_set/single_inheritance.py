class A :
    def __init__(self,name):
        self.name = name
    def show(self):
        print("hello " + self.name + " !!")

class B(A) :
    def display(self):
        print("it's child class..")

b1 = B("Sayma")
b1.show()
b1.display()

