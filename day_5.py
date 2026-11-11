x = int(input("Enter a number in the range 1-10: "))

for i in range(1,11):
    print(x,"x",i,"=",x*i)

password = input("Enter password(type 'exit' to quit): ")
while password != "exit":
    print("Wrong password, try again.")
    password = input("Enter password(type 'exit' to quit): ")
print("Goodbye!")