#number validation
def get_valid_intege(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return integer
            else:
                print(f"Error: Input must be between {min_value} and {max_value}.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")
integer_prompt = ("Enter am integer between 1 an integer")
valid_integer =  get_valid_intege(integer_prompt, 1, 100)
print(valid_integer)

#create a unction with  variabel-length
def print_student_info(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_student_info("Charlie", age=15, grade="10th", city="london")

#create a function to sort data with custom key
def sort_strings_by_length(strings):
    return sorted(strings, key=len)
strings = ["apple", "banana","orange","kiwi","grape"]
sorted_strings = sort_strings_by_length(strings)
print(f"Strings sortedbylength: {sorted_strings}")

# Create a function to transform data with conditional logic
def classify_numbers(numbers):
    classified = {
        'even' : [num for num in numbers if num %2 == 0],
        'odd' : [num for num in numbers if num %2 != 0]
    }
    return classified

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
classified_numbers = classify_numbers(numbers)
print(f"Classified numbers: {classified_numbers}")

# Create a function to Agregate Data with Custom Operations
import math
def calculate_product(numberss):
    product_multiple = math.prod(numberss)
    return product_multiple

numberss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = calculate_product(numberss)
print(f"Product of numbers: {product}")

#create a function to combine data
def merge_list(list1, list2):
    merged_list = list1 + list2
    return list(set(merged_list))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers =  [1, 3, 5, 7, 9, 11]
merged_list =  merge_list(numbers, odd_numbers)
print(f"Merged list: {merged_list}")

