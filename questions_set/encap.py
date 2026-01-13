# Public members
class student :
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def show(self):
        print(self.name,self.age)

s1 = student("Sayma",18)
s1.show()

#direct access
print(s1.name)
print(s1.age)

#protected members 
class flower :
    def __init__(self,fav_flower,color):
        self._fav_flower = fav_flower 
        self.color =color

class info(flower):
    def show(self):
        print(self._fav_flower,self.color)

f1 = info("lily","white")
f1.show()

print(f1._fav_flower)
print(f1.color)  

#private members 
class account :
    def __init__(self, balance):
        self.__balance = balance
        
    def show(self):
        return self.__balance
    
    def deposite(self, amount):
        self.__balance += amount

a1 = account(5000)
print(a1.show())

a1.deposite(200)
print(a1.show())