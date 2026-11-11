x = int(input("Enter a number x: "))

if x < 0:
    print("The number is negative!")
elif x == 0:
    print("The number is zero!")
else:
    print("The number is positive!")

if x % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")