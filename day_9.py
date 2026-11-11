phonebook = {"Paul": "0612345678", "Marie": "0698765432"}
print("Starting phonebook: ", phonebook)

phonebook["Julie"] = "0611223344"
print("After adding Julie: ", phonebook)

print("Marie's number: ", phonebook["Marie"])

del phonebook["Paul"]
print("After deleting Paul: ", phonebook)

for name, number in phonebook.items():
    print(f"{name}: {number}")