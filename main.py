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

#_______________________________________________________
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

#passing lambda function to map
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

#Typecasting str()/ int()/float()/bool()
num = 10
print(type(num))
num = str(num)
print(type(num))    

#User input
name = input("What is your name? ")
print(f"Hello {name}, welcome to the program!")

print("Hi, I am your AI virtual shopping mall, would you like to buy something?")
response = input("Please enter your choice: ")
print(f"You chose: {response}")
item_list = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Here is the list of items available for purchase:")
for item in item_list:
    print(item)
price_list = [1.5, 0.5, 2.0, 1.0, 3.0]
item_dict = dict(zip(item_list, price_list))
total_price = 0
while True:
    item_choice = input("Enter the item you want to buy (or type 'done' to finish): ")
    if item_choice.lower() == 'done':
        break
    if item_choice in item_dict:
        total_price += item_dict[item_choice]
        print(f"{item_choice} added to your cart. Current total: ${total_price:.2f}")
    else:
        print("Item not found. Please choose from the available items.")
print(f"Your total purchase amount is: ${total_price:.2f}. Thank you  for shopping with us!")