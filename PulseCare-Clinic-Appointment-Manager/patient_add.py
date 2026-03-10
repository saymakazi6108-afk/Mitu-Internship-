class Patient:
    def __init__(self, name, age, emergency=0):
        self.name = name
        self.age = age
        self.emergency = emergency
        self.status = "waiting"
