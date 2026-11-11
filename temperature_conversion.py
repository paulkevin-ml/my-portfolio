choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius?")
temp = float(input("Enter the temperature: "))
if choice == "C":
    F = temp*1.8+32
    print("The temperature in Fahrenheit is:", F)
elif choice == "F":
    C = (temp-32)*5/9
    print("The temperature in Celsius is:", C)
else:
    print("Please try again!")