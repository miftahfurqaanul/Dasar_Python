# Function to return the sum of two numbers
def add_two_numbers(a, b):
    return a + b

# Test the function with different values
test_values = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Loop through the test values and print the results
for a, b in test_values:
    result = add_two_numbers(a, b)
    print(f"The sum of {a} and {b} is {result}")