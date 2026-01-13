class car :
    def __init__(self,name):
        self.name = name

class BMW(car):
    
    def show(self):
        print(self.name) 

b1 = BMW("BMW")
b1.show()