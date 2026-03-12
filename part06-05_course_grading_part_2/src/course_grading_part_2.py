# write your solution here
if True:
    student_info = input("Student information: ")
    exercises_completed = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercises_completed = "exercises1.csv"
    exam_points = "exam_points1.csv"

names = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2]
exercise_points = {}
with open(exercises_completed) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum_exercise = 0
        for number in parts[1:]:
            sum_exercise += int(number)
        exercise_points[parts[0]] = sum_exercise // 4
exm_points = {}
with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum_notes = 0
        for note in parts[1:]:
            sum_notes += int(note)
        exm_points[parts[0]] = sum_notes
grades = {}
for ident, points in exercise_points.items():
    if ident in exm_points:
       total_points = exm_points[ident] + points
    
    if total_points >= 28:
        grades[ident] = 5
    elif total_points >= 24:
        grades[ident] = 4
    elif total_points >= 21:
        grades[ident] = 3
    elif total_points >= 18:
        grades[ident] = 2
    elif total_points >= 15:
        grades[ident] = 1
    else:
        grades[ident] = 0

for ident , grade in grades.items():
    if ident in names:
        name = names[ident]
        print(f"{name} {grade}")