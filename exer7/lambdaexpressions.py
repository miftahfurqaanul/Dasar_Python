# Function that takes a list of numbers and a callback function
def apply_callback(numbers, callback):
    # Apply the callback function to each element in the list
    return [callback(num) for num in numbers]

# Test the function with a list of numbers and a lambda expression for squaring
numbers_list = [1, 2, 3, 4, 5]

# Applying the lambda expression as the callback to square each number
result = apply_callback(numbers_list, lambda num: num ** 2)

# Print the result
print(f"Original list: {numbers_list}")
print(f"List after applying the lambda square callback: {result}")