import os
FILE = "expenses.txt"
def load_expenses():
    expenses = []
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            for line in f:
                line = line.strip()
                amount,category = line.split(",")
                expenses.append({"amount":float(amount),"category":category})
    return expenses
def save_expenses(expenses):
     with open(FILE, "w") as f:
         for expense in expenses:
             f.write(str(expense["amount"])+ "," +expense["category"]+ "\n")
def add_expense(expenses, amount, category):
    expenses.append({"amount":amount, "category":category})
    save_expenses(expenses)
def view_total(expenses):
    total = 0     
    for expense in expenses:
        total = total + expense["amount"]
    print(f"Total spent:{total}")
def view_by_category(expenses):
    totals = {}
    for expense in expenses:
        cat = expense["category"]
        if cat in totals:
            totals[cat]=totals[cat]+expense["amount"]
        else:
            totals[cat]=expense["amount"]
    for cat, amount in totals.items():
        print(f"{cat}:{amount}")
expenses = load_expenses()
while True:
    print("\n1)Add Expense 2)View Total 3)View by Category 4)Quit")    
    choice = input("Choose an option: ")
    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        add_expense(expenses,amount,category)
    elif choice == "2":
        view_total(expenses)    
    elif choice =="3":
        view_by_category(expenses)
    elif choice =="4":
        break
    else:
        print("Invalid option")