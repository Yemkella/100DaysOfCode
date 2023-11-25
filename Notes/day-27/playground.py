#Example of unlimited arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1,3,2,5,5,2))


#Examples of key word arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get["make"]
        self.model = kw.get("model")
        self.color = kw.get["color"]
        self.seats = ke.get["seats"]

my_car = Car(make="Nissan", model="GT-R")