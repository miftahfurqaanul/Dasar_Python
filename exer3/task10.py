def calculate_average(numbers):

    if not numbers:
        return None  # Handle empty list

    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("The average of the numbers is:", average)