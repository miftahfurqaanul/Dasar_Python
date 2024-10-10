fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange",
    "kiwi": "green"
}

# Print each key-value pair in the dictionary
for fruit, color in fruits.items():
    print(f"{fruit} is {color}.")

# Check if a specific fruit is in the dictionary
target_fruit = "mango"
if target_fruit in fruits:
    print(f"{target_fruit} is {fruits[target_fruit]}.")
else:
    print(f"{target_fruit} is not in the dictionary.")

# Add a new fruit-color pair
fruits["strawberry"] = "red"
print("Updated dictionary:", fruits)