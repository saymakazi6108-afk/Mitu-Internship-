class car :
    def __init__(self,name):
        self.name = name

class BMW(car):
    def __init__(self, name , model):
        super().__init__(name)
        self.model = model

    def show(self):
        print(self.name,self.model) 

b1 = BMW("BMW","M8")
b1.show()