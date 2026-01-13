class car : 
	def show(self, name): 
		self.name = name
		print("I have " + self.name + " car. ")
	
C1 = car()
C1.show("BMW")

C2 = car()
C2.show("PORSCHE")  

C3 = car()
C3.show("THAR") 


class student :
	name = "unknown" # class attribute 
	
	def __init__(self , name):
		self.name = name # instance attribute 
		
	def show(self):
			print(self.name)
	
s1 = student("Sayma")

print(s1.name) # priority : instance attribute > class attribute 
print(student.name) # calling class attribute if both have name 
s1.show()


class person :
	def __init__(self):
		self.name = "unknown" 
	
	def show(self) : 
		print(self.name)
	
p1 = person()
p1.show()

class flower :
	def __init__(self , name , color):
		self.name = name 
		self.color = color

	def display(self) :
		print("I want " + self.name + " with " + self.color +" color")

f1 = flower("rose" , "white")
f1.display()

class interns:
	def __init__(self , name, company ="Mitu Skillologies", interval = "6"):
		self.name = name 
		self.company = company
		self.interval = interval
	
	def info(self):
		print("I'm "+self.name)
		print("Currently, I'm working as an intern in "+self.company+
		" for "+self.interval+" months duration")

i1 = interns("Sayma Kazi")
i1.info()
