school_data = {
    "Ali": {
        "grades" : [85, 90, 88],
        "attendance" : 95
    },
    "Bagus": {
        "grades" : [92, 88, 79],
        "attendance" : 88
    },
    "Caca": {
        "grades" : [78, 85, 90],
        "attendance" : 99
    },
    "David": {
        "grades" : [88, 76, 90],
        "attendance" : 85
    }
}
school_data["Evan"] = {
    "grades" : [91, 85, 87],
        "attendance" : 90
}
for student, data in  school_data.items():
    avg_grade = sum(data["grades"]) /  len(data["grades"])
    data["attendance"] += data["attendance"]  * 0.2
    if data["attendance"] > 100:
        data["attendance"] = 100
    print(f"student: {student}, Average Grade: {avg_grade:.2f},  Attendance: {data['attendance']}%")

for student,  data in school_data.items():
    if data["attendance"] < 90:
        print(f"Student: {student} has good attendance")
        del  school_data[student]




