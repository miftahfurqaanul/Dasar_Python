student_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 75

}

student_grades["David"] = 89

print(student_grades["Bob"])

if " Ali" in student_grades:
    print("Ali is in the dictionary. ")
else:
    print("Ali is not in the dictionary. ")
del student_grades["Chalie"]

for student, grade  in student_grades.item():
    print(f"{student} has a grade of {grade}.")