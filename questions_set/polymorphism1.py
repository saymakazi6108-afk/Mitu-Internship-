#function polymorphism 
print(len("Sayma Kazi"))
print(len([12,94,71,50]))
print(len((2,4)))


# method overloading 
class sumation:
    def add(self, a, b=0, c=0):
        return a + b + c

s1 = sumation()
print(s1.add(4))
print(s1.add(4,6))
print(s1.add(7,3,4))

# Method overriding 
class animal :
    def sound(self):
        print("animal makes sound")

class cat(animal):
    def sound(self):
        print("cat meows")

class dog(animal):
    def sound(self):
        super().sound()
        print("dog barks")

c1 = cat()
c1.sound()

d1 = dog()
d1.sound()

#operator overloading 

print('a' + 'b')
print(23 + 65 + 49)
print("Sayma" + "Kazi")
print((34,67) + (21,95))

#Duck typing 

class student :
    def work(self):
        print("Student is studying")

class employee :
    def work(self):
        print("Employee is working")

class teacher :
    def work(self):
        print("Teacher is teaching")

def do_work(person):
    person.work()

do_work(student())
do_work(employee())
do_work(teacher())
