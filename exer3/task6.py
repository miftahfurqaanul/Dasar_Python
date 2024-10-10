# Create a string variable with your name
name = "Miftah Furqaanul Haq"

# Use a for-loop to print each character in your name
for char in name:
    print(char)

# Count and print the number of vowels (aeiou) in your name
vowel_count = 0
for char in name:
    if char in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)

# Print the index of the first occurrence of the letter 'e' in your name
e_index = name.find('e')
print("Index of the first occurrence of 'e':", e_index)

