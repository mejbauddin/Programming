a,b = 1,2
print(a,b)

a,b = b,a # The value of the variables a and b are swapped.

print(a,b)

# Function
def Hello_world():
    print("Hello world")

# Function with Argument 
def Hello_World(ID, Name, Dept):
    print(f"Hello {Name}! This is your Student ID : {ID} and Major : {Dept}")

Hello_world()
Hello_World(1234567890, "Mejbah", "Software")


# Function Argument wit default Value 
def Country_Function(Country="Bangladesh"):
    print(f"I\'m from {Country}")

Country_Function()
Country_Function("China")