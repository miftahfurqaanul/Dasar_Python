people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 20},
    {"name": "Eve", "age": 28}
]

# Print names of people who are 25 years old or older
for person in people:
    if person["age"] >= 25:
        print(person["name"])

# Calculate and print the average age
total_age = 0
num_people = len(people)
for person in people:
    total_age += person["age"]
average_age = total_age / num_people
print("Average age:", average_age)

# Add a new person to the list
new_person = {"name": "Frank", "age": 22}
people.append(new_person)
print("Updated list:", people)