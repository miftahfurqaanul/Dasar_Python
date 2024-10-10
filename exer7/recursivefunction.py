# Recursive function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Test the function with different numbers
test_numbers = [0, 1, 5, 7, 10]

# Print the results
for number in test_numbers:
    result = factorial(number)
    print(f"Factorial of {number} is {result}")