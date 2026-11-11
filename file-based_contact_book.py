import os
FILE = "contacts.txt"
def load_contacts():
    contacts=[]
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
             for line in f:
                 line = line.strip()
                 name,phone = line.split(",")
                 contacts.append({"name": name, "phone": phone})
    return contacts        
def save_contacts(contacts):
     with open(FILE, "w") as f:
         for contact in contacts:
             f.write(contact["name"]+","+contact["phone"]+"\n")
def add_contact(contacts, name, phone):
    contacts.append({"name":name, "phone":phone})
    save_contacts(contacts)
contacts = load_contacts()
while True:
    print("\n1)Add 2)View 3)Search 4)Quit")
    choice = input("Choose an option")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        add_contact(contacts,name,phone)
    elif choice == "2":
        for c in contacts:
            print(f"{c['name']}:{c['phone']}")
    elif choice == "3":
         search = input("Enter the name you want to search: ")
         for c in contacts:
            if c["name"] == search:
                print(f"{c['name']}:{c['phone']}")
    elif choice == "4":
        break
    else:
        print("Invalid option")    