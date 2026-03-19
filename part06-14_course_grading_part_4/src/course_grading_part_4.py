if True:
    student_informations = input("Student information: ")
    exercises_completed = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_information = input("Course information: ")
else:
    student_informations = "students1.csv"
    exercises_completed = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_information = "course1.txt"

with open(course_information) as f:
    first_line = ""
    attemps = 1
    for line in f:
        if attemps == 1:
            find = line.find(" ")
            first_line += line[find+1:-1]+", "
        else:
            parts = line.strip().split(" ")
            first_line += parts[-1] + " credits\n"
        attemps+=1

student_inf = {}
with open(student_informations) as f:
    for line in f:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        student_inf[parts[0]] = f"{parts[1]} {parts[2]}"

exe_nbr = {}
exe_pts = {}
with open(exercises_completed) as f:
    for line in f:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exer_nombre = 0
        for part in parts[1:]:
            exer_nombre += int(part)
        exe_nbr[parts[0]] = exer_nombre
        exe_pts[parts[0]] = exer_nombre // 4

exm_pts = {}
with open(exam_points) as f:
    for line in f:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exam_pts = 0
        for part in parts[1:]:
            exam_pts += int(part)
        exm_pts[parts[0]] = exam_pts

grades = {}
total_pts = {}
for ident, points in exe_pts.items():
    if ident in exm_pts:
       total_pts[ident] = exm_pts[ident] + points
    
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

with open("results.txt", "w") as f:
    f.write(first_line)
    f.write(f"{(len(first_line)-1)*"="}\n")
    f.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n")
    for ident , name in student_inf.items():
        if ident in exe_nbr:
            exer_nbr = exe_nbr[ident]
        if ident in exe_pts:
            exer_pt = exe_pts[ident]
        if ident in exm_pts:
            exam_pt = exm_pts[ident]
        if ident in grades:
            grade = grades[ident]
        if ident in total_pts:
            total_point = total_pts[ident]
        f.write(f"{name:30}{exer_nbr:<10}{exer_pt:<10}{exam_pt:<10}{total_point:<10}{grade:<10}\n")

with open("results.csv", "w") as f:
    for ident , name in student_inf.items():
        if ident in grades:
            f.write(f"{ident};{name};{grades[ident]}\n")
