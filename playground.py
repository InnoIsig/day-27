def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add( 3, 4, 5, 6))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
