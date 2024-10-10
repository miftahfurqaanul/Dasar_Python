people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 20),
    ("Eve", 28)
]

sorted_people = sorted(people, key=lambda person: person[1])

print(sorted_people)