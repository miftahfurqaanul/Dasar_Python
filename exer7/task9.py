def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        return None  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

def filter_numbers_above_threshold(numbers, threshold):
    """Filters out numbers below a certain threshold from a list."""
    filtered_numbers = [num for num in numbers if num > threshold]
    return filtered_numbers

# Test data
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
threshold = 50

# Calculate average of all numbers
average_all = calculate_average(numbers)
print("Average of all numbers:", average_all)

# Filter numbers above threshold
filtered_numbers = filter_numbers_above_threshold(numbers, threshold)
print("Numbers above threshold:", filtered_numbers)

# Calculate average of numbers above threshold
average_above_threshold = calculate_average(filtered_numbers)
print("Average of numbers above threshold:", average_above_threshold)