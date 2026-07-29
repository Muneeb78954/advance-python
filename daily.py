class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    def sound(self):
        print("Some generic animal sound")

 #Inheritance 
class Reptiles(Animal):
    def sound(self):              # Polymorphism
        print("Hissssss")

class Mammals(Animal):
    def sound(self):              # Polymorphism
            print("Roarrrrrr")

class Birds(Animal):
    def sound(self):              # Polymorphism
            print("Chirppp")


lion = Mammals("Lion", "Mammal")
sparrow = Birds("Sparrow", "Bird")
snake = Reptiles("Snake", "Reptile")

print(lion.name)

lion.sound()
sparrow.sound()
snake.sound()