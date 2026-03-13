if True:
    student_info = input("Student information: ")
    exercises_completed = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercises_completed = "exercises1.csv"
    exam_points = "exam_points1.csv"

students = {}
with open(student_info) as f:
    for line in f:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]

exercises_nbr = {}
exercises_pts = {}
with open(exercises_completed) as f:
    for line in f:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exec_nbr = 0
        for nb in parts[1:]:
            exec_nbr += int(nb)
        exercises_nbr[parts[0]] = exec_nbr
        exercises_pts[parts[0]] = exec_nbr // 4

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
total_pts = {}
for ident, points in exercises_pts.items():
    if ident in exm_points:
       total_pts[ident] = exm_points[ident] + points
    
    if total_pts[ident] >= 28:
        grades[ident] = 5
    elif total_pts[ident] >= 24:
        grades[ident] = 4
    elif total_pts[ident] >= 21:
        grades[ident] = 3
    elif total_pts[ident] >= 18:
        grades[ident] = 2
    elif total_pts[ident] >= 15:
        grades[ident] = 1
    else:
        grades[ident] = 0
print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")
for ident , name in students.items():
    if ident in exercises_nbr:
        exer_nbr = exercises_nbr[ident]
    if ident in exercises_pts:
        exer_pt = exercises_pts[ident]
    if ident in exm_points:
        exam_pt = exm_points[ident]
    if ident in grades:
        grade = grades[ident]
    if ident in total_pts:
        total_point = total_pts[ident]
    print(f"{name:30}{exer_nbr:<10}{exer_pt:<10}{exam_pt:<10}{total_point:<10}{grade:<10}")
