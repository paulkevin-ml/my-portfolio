import math_utils

print(math_utils.add(5,3))
print(math_utils.subtract(10,4))
print(math_utils.multiply(6,7))

x = 10

def show_scope():
    x=5
    print("Inside function, x =", x)
show_scope()
print("Outside function, x =", x)