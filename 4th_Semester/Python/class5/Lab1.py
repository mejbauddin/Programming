# Task 6. Define two variables and print their sum.

a = 10
b = 20
print(a + b)

# Task 7. Demonstrate dynamic typing (a variable can reference different types).

x = 10
print(type(x))
x = "Python"
print(type(x))

# Task 8. Print object identities using id().
a = 100
b = 100
print(id(a))
print(id(b))

# Task 9. Modify a and observe whether the object identity changes.

a = a + 1
print(a)
print(id(a))

# Task 10. Compare value equality (==) vs object identity (is).
x = 5
y = 5
print(x == y)
print(x is y)

# Task 11. Check the Boolean value of different objects.
print("# Task 11. Check the Boolean value of different objects.")
print(bool(0))
print(bool(1))
print(bool(''))
print(bool("Python"))
print(bool([]))
print(bool([1,2]))

#Task 12. Implement a calculator that supports +, -, *, and /. It must handle division by zero.
print("Calculator")
number_1 = float(input('Enter first number: '))
number_2 = float(input('Enter second number: '))
mathTry = input('What Do you want to do? Select (+, -, *, /): ')

if mathTry == '+':
    print(f'{number_1} {mathTry} {number_2} =', number_1 + number_2)
elif mathTry == '-':
    print(f'{number_1} {mathTry} {number_2} =', number_1 - number_2)
elif mathTry == '*':
    print(f'{number_1} {mathTry} {number_2} =', number_1 * number_2)
elif mathTry == '/':
    if number_2 != 0:
        print(f'{number_1} {mathTry} {number_2} =', number_1 / number_2)
    else:
        print('Error: Division by zero')
else:
    print('Error: Invalid operator')

