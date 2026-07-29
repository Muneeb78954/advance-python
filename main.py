names = ["Muneeb", "Bilal", "Haider", "Hassan", "Mujtaba", "Malaika", "Zain"]


m_names = []
for name in names:
    if "M" in name:
        m_names.append(name)
print(m_names)


"""List comprehension"""
m_names = [name for name in names if "M" in name]
print(m_names)


def avg(num1, num2):
    return (num1 + num2) / 2


print(avg(10, 20))


"""Lamba function"""
avg_lambda = lambda num1, num2: (num1 + num2) / 2
print(avg_lambda(10, 20))

"""Passing function as an argument"""
plus = lambda x, y: x + y


def calc(x, plus):
    return x * plus(20, 10)


print(calc(5, plus))

"""Anonymous function"""


def anonymous(fx, value):
    return 10 + fx(value)


print(anonymous(lambda x: x * x, 2))


# _______________________________________________________
def cube(x):
    return x * x * x


print(cube(3))

numbers = [23, 45, 67, 89, 12, 34, 56]
# new_list = []
# for i in numbers:
#     new_list.append(cube(i))
# print(new_list)

"""Map function"""
new_list = list(map(cube, numbers))
print(new_list)

# passing lambda function to map
new_new_list = list(map(lambda x: x * x, numbers))
print(new_new_list)
"""Filter function"""
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filter_even(x):
    return x % 2 == 0


even_list = list(filter(filter_even, num))
print(even_list)

""""Reduce function"""
from functools import reduce

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sum = reduce(lambda x, y: x + y, num1)
print(sum)

# Typecasting str()/ int()/float()/bool()
num = 10
print(type(num))
num = str(num)
print(type(num))

# built in math functions
import math

x = 3.14
y = -7
z = 10
print(round(x))
print(abs(y))
print(pow(z, 2))
print(max(x, y, z))
print(min(x, y, z))

print(math.sqrt(z))
print(math.pi)
print(math.e)
print(math.factorial(5))
print(math.ceil(x))
print(math.floor(x))

# ternary operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)


tup = (("BoB", "RoB"), ("Chachu", "Mamu"))

tup[1]

# eliminate the need of number of arguments 
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(2,3,4,5,6,67,7))

def address(**kwargs):
    for key , values in kwargs.items():
        print(f"{key}: {values}")

address(street = "123 LA", province ="Punjab", city ="Lahore")

def day_of_week(day):
    match day:
        case 1:
            return "It is Monday!"
        case 2:
            return "It is Tuesday!"
        case 3:
            return "It is Wednesday!"
        case 4:
            return "It is Thursday!"
        case 5:
            return "It is Friday!"
        case 6: 
            return "It is Satureday!"
        case 7:
            return "It is Sunday!"
        case _:
            return "It is not a valid day!"
day_of_week(7)


# OOP
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
