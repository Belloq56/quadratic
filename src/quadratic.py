'''Quadratic.py solves ax^2+bx+c=0 and returns the result'''

import numpy as np

a = float(input("Enter a: "))
print(a+5)
b = float(input("Now, enter b: "))
c = float(input("Finally, enter c: "))

x1 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-np.sqrt(b**2-4*a*c))/(2*a)
print("Your x values are ",x1,"and ",x2)