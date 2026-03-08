# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []
    return students

def add_course(students, name, complete_course_grade):
    repeat_course = 0
    
    for item in students[name]:
        if item[0] == complete_course_grade[0]:
            if complete_course_grade[1] > item[1] :
                students[name].remove(item)
                students[name].append(complete_course_grade)
            
            repeat_course += 1
    if complete_course_grade[1] != 0 and repeat_course == 0:
        students[name].append(complete_course_grade)
        
    return students


def print_student(students: dict, name: str):
    if name in students:
        list_student = students[name]
        completed_courses = len(list_student)
        sum_grade = 0
        if list_student == []:
            print(f"{name}:")
            print(" no completed courses")
        else:
            print(f"{name}:")
            print(f" {completed_courses} completed courses:")
            for item in list_student:
                print(f"  {item[0]} {item[1]}")
                sum_grade += item[1]
            avg_grade = sum_grade / completed_courses
            print(f" average grade {avg_grade}")
            
    else:
        print(f"{name}: no such person in the database")
def summary(students):
    print(f"students {len(students)}")
    most_courses_name = ""
    most_courses_completed = 0
    best_avg_name = ""
    best_evg_grade = 0
    for student, value in students.items():
        if len(value) > most_courses_completed:
            most_courses_completed = len(value)
            most_courses_name = student
        sum_grade = 0
        for item in value:
            sum_grade += item[1]
        avg_grade = sum_grade / len(value)
        if avg_grade > best_evg_grade:
            best_evg_grade = avg_grade
            best_avg_name = student
    print(f"most courses completed {most_courses_completed} {most_courses_name}")
    print(f"best average grade {best_evg_grade} {best_avg_name}")
             

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")
