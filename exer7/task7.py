# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if not numbers:  # Check if the list is empty
        return 0
    return sum(numbers) / len(numbers)

# Function to filter out numbers below a certain threshold
def filter_below_threshold(numbers, threshold):
    return [num for num in numbers if num >= threshold]

# Test both functions on a list of numeric data
numbers_list = [3, 10, 6, 2, 7, 8, 12, 1, 9, 5]
threshold = 6

# Calculate the average of the entire list
average_all = calculate_average(numbers_list)
print(f"Average of all numbers: {average_all}")

# Filter numbers above the threshold and calculate the average
filtered_numbers = filter_below_threshold(numbers_list, threshold)
average_filtered = calculate_average(filtered_numbers)

print(f"Numbers above or equal to the threshold of {threshold}: {filtered_numbers}")
print(f"Average of numbers above the threshold: {average_filtered}")