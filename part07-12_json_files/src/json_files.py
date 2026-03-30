# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as f:
        data = f.read()
    
    students = json.loads(data)

    for student in students:
        hobbies = ", ".join(student["hobbies"])

        print(f"{student["name"]} {student["age"]} years ({hobbies})")

print_persons("file1.json")