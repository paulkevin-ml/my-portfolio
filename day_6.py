List = []

option = input("Do you want to 1) Add one item__2) Remove one item__3) Sort the list?")

if option == "1":
    new_item = input("Add an item: ")
    List.append(new_item)
elif option == "2":
    item_to_remove = input("Remove an item: ")
    List.remove(item_to_remove)
elif option == "3":
    List.sort
else:
    print("Try again")