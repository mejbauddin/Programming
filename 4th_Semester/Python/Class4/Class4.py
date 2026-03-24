import random
class Person:
    # Say Hello or Printing some
    def sayHello(self):
        print("Hello, how are you?")

    # For Random Number 
    def randomf(self):
        print(random.random())


p = Person()

p.randomf()
p.sayHello()

x = 100

if x > 20:
    print("Above ten")
    if x > 24:
        print("24")

    elif x < 77:
        print("77")
    else: 
        print("!!!!!!!!!!")


fruits = ["apple","banana","cherry"]

for x in fruits:
    print(x)

for x in "fruits":
    print(x)