def apply_callback(numbers, callback):
    """Applies a callback function to each element of a list and returns a new list."""
    new_list = []
    for num in numbers:
        if callback(num):
            new_list.append(num)
    return new_list

def is_greater_than_5(num):
    """Checks if a number is greater than 5."""
    return num > 5

# Test data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Apply the callback function
result = apply_callback(numbers, is_greater_than_5)

print("Numbers greater than 5:", result)