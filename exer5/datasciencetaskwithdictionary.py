students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 75,
    "David": 95,
    "Eve": 80
}

# Calculate and print the average score
total_score = 0
num_students = len(students)
for score in students.values():
    total_score += score
average_score = total_score / num_students
print("Average score:", average_score)

# Identify and print the student with the highest score
highest_score = max(students.values())
for student, score in students.items():
    if score == highest_score:
        print("Student with the highest score:", student)

# Add a new student and score
students["Frank"] = 88
print("Updated dictionary:", students)