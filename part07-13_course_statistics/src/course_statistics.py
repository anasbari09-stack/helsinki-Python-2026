# Write your solution here
import urllib.request
import json
def retrieve_all():
    active_courses = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    for course in courses:
        if course['enabled']:
            sum_exercise = sum(course["exercises"])
            active_courses.append((course["fullName"], course["name"], course["year"], sum_exercise))
    return active_courses

def retrieve_course(course_name: str):
    course_dic = {}
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    statics_course = json.loads(data)
    course_dic['weeks'] = len(statics_course)
    max_students = 0
    hour_total = 0
    exercise_total = 0
    for key, static in statics_course.items():
        if static['students'] > max_students:
            max_students = static['students']
        hour_total += static['hour_total']
        exercise_total += static['exercise_total']
        
    
    course_dic['students'] = max_students
    course_dic['hours'] = hour_total
    course_dic['hours_average'] = hour_total // max_students
    course_dic['exercises'] = exercise_total
    course_dic['exercises_average'] = exercise_total // max_students
    return course_dic

