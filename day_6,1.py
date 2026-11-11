foods = ["pizza","pasta", "sushi", "tacos", "burgers"]
print("Starting list: ", foods)

foods.append("ice cream")
print("After adding: ", foods)

foods.remove("tacos")
print("After removing: ", foods)

foods.sort()
print("After sorting: ", foods)

def find_largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n>largest:
            largest = n
    return largest

test_list = [-5,12,0,-100,47]
print(find_largest(test_list))