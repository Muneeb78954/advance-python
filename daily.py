class car:
    def __init__(self, model, year, color, engine, speed, for_sale, price):
        self.model = model
        self.year = year
        self.color = color 
        self.engine = engine
        self.speed = speed
        self.for_sale = for_sale 
        self.price = price

    def drive(self):
        print(f"You Drive The {self.color} {self.model}!")

    def stop(self):
        print(f"You Stop The {self.color} {self.model}!")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = car("Bughati", 2025, "Carbon Black", "V12", "235 Km/h", False, "$1.33M")
car2 = car("Mercedes", 2026, "Silver", "V8", "195 Km/h", False, "$145K")
car3 = car("BMW", 2026, "Red", "V8", "160 Km/h", False, "$90k")

print(car1.model)
print(car2.price)

car1.drive()
car1.stop()

car3.describe()

class Student:
    def __init__(self, sid, name, age, major, section, marks, performance):
        self.sid         = sid
        self.name        = name 
        self.age         = age
        self.major       = major
        self.section     = section
        self.marks       = marks
        self.performance = performance
    def study(self):
        print(f"{self.name} is studying in the class!")

    def play(self):
        print(f"{self.name} is playing in the playground!")

    def test(self):
        print(f"{self.name} is in the test!")

    def remarks(self):
        print(f"{self.name} obtained {self.marks} marks. No dought {self.name} is {self.performance}")


student1 = Student(12, 
                   "Muneeb", 
                   22, 
                   "Computer Science", 
                   "V1", 
                   89, 
                   "Great Student")

print(student1.name)
print(student1.marks)
print(student1.section)

student1.study()
student1.remarks()
