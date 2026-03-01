# Write your solution here
def inputs_points_exercises():
    students_list = []
    while True:
        exa_points_exe_completed = input("Exam points and exercises completed: ")  
        if exa_points_exe_completed == "" :
            break
        students_list.append(exa_points_exe_completed)
    return students_list

def main():
    # sparate exam points and exercise comleted in differece lists
    exam_points = []
    exercises_completed = []
    for item in inputs_points_exercises():
        sparate = item.split(" ")
        exam_points.append(int(sparate[0]))
        exercises_completed.append(int(sparate[1]))
    # transform exercise completed to points
    exercises_completed_points = []
    for item in exercises_completed:
        if item == 100:
            exercises_completed_points.append(10)
        elif item >= 90:
            exercises_completed_points.append(9)
        elif item >= 80:
            exercises_completed_points.append(8)
        elif item >= 70:
            exercises_completed_points.append(7)
        elif item >= 60:
            exercises_completed_points.append(6)
        elif item >= 50:
            exercises_completed_points.append(5)
        elif item >= 40:
            exercises_completed_points.append(4)
        elif item >= 30:
            exercises_completed_points.append(3)
        elif item >= 20:
            exercises_completed_points.append(2)
        elif item >= 10:
            exercises_completed_points.append(1)
        else:
            exercises_completed_points.append(0)
    
    # calculate total points(add exercise completed point to exam points
    # and give a grade
    total_points = []
    grade = []
    student_pass = 0
    for i in range(0,len(exercises_completed_points)):
        total_points.append(exercises_completed_points[i] + exam_points[i])
        if exam_points[i] < 10:
            grade.append(0)
        elif 14 >= total_points[i] >= 0:
            grade.append(0)
        elif 17 >= total_points[i] >= 15:
            grade.append(1)
            student_pass += 1
        elif 20 >= total_points[i] >= 18:
            grade.append(2)
            student_pass += 1
        elif 23 >= total_points[i] >= 21:
            grade.append(3)
            student_pass += 1
        elif 27 >= total_points[i] >= 24:
            grade.append(4)
            student_pass += 1
        elif 30 >= total_points[i] >= 28:
            grade.append(5)
            student_pass += 1
    # calculate statics and print result for user
    Points_average = sum(total_points) / len(total_points)
    pass_percentage = (student_pass * 100) / len(total_points)
    print("Statistics:")
    print(f"Points average: {Points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    print(f"  5: {"*" * grade.count(5)}")
    print(f"  4: {"*" * grade.count(4)}")
    print(f"  3: {"*" * grade.count(3)}")
    print(f"  2: {"*" * grade.count(2)}")
    print(f"  1: {"*" * grade.count(1)}")
    print(f"  0: {"*" * grade.count(0)}")
main()


        












    


