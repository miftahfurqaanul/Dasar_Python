# Function that takes a list of numbers and a callback function
def apply_callback(numbers, callback):
    # Apply the callback function to each element in the list
    return [callback(num) for num in numbers]

# Callback function that squares a number
def square(num):
    return num ** 2

# Test the function with a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Applying the square callback to each element in the list
result = apply_callback(numbers_list, square)

# Print the result
print(f"Original list: {numbers_list}")
print(f"List after applying the square callback: {result}")