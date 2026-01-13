class animal:
    def sound(self):
        print("Animal sound")

class dog(animal):
    def dog_sound(self):
        super().sound()
        print("Dog barks")

d1 = dog()
d1.dog_sound()