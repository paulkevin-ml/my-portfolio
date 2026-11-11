def safe_divide(a,b):
    try:
        result = a/b
        print("Result: ", result)
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")

safe_divide(10,2)
safe_divide(5,0)

while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print("You entered: ", number)
        break
    except ValueError:
        print("That's not a valid number, try again.")