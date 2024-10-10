mixed_tuple = (10, 20.5, "Hello", 30, "World", 40.7)

# Print each element and its data type
for element in mixed_tuple:
    print(f"{element} is of type {type(element)}")

# Calculate the sum of numeric elements
numeric_sum = 0
for element in mixed_tuple:
    if isinstance(element, (int, float)):
        numeric_sum += element
print("Sum of numeric elements:", numeric_sum)

# Convert each element to string and store in a new tuple
string_tuple = tuple(map(str, mixed_tuple))
print("Original tuple:", mixed_tuple)
print("Tuple of string elements:", string_tuple)