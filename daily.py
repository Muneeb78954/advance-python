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
                 