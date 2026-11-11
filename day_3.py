weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = weight/ (height**2)

result = print(f"Your BMI is: {round(BMI,1)}")

if BMI < 18.5:
    print("You're underweight.")
elif BMI < 25:
    print("You're normal.")
elif BMI >= 25.0:
    print("You're overweight.")
else:
    print("try again.")
