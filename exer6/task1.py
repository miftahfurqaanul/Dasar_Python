numbers = [41, 5, 1, 3, 89, 32]

min_number = numbers[0]
max_number = numbers[0]

for  number in numbers:
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number

print(" the smallest number is: ", min_number)
print(" the largest number is: ", max_number)