#(a+b+c)/2
#root (h*(h-a)*(h-b)*(h-c))

import math

a= 12
b= 34
c= 45
h = (a+b+c)/2
area = math.sqrt(h*(h-a)*(h-b)*(h-c))
print(f"This is area : {area}")


print(type(print))
print(id(123))
a= 123
print(id(a))

a = 2
b = 3
t = a
a = b
b = t
