#1
# list_of_number = [1, 2, 3, 4, 5]

#2
# for number in list_of_number:
#     print(number)

#3
# Initialize the sum variable
total_sum = 0

# Use a for loop to calculate the sum
for number in range(1, 6):  # range(1, 6) generates numbers 1 to 5
    total_sum += number

# Print the result
print("The sum of numbers from 1 to 5 is:", total_sum)

#4
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a for loop to square each number and print the result
for number in numbers:
    squared = number ** 2  # Square the number
    print(squared)