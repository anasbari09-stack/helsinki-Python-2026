# Write your solution here
from datetime import datetime
def cheaters():
    student_times = {}
    with open("start_times.csv") as f:
        for line in f:
            parts = line.strip().split(";")
            student_times[parts[0]] = []
            start_time = datetime.strptime(parts[1], "%H:%M")
            student_times[parts[0]].append(start_time)

    with open("submissions.csv") as file:
        for line in file:
            parts = line.strip().split(";")
            task_time = datetime.strptime(parts[3], "%H:%M")
            student_times[parts[0]].append(task_time)
    cheated_students = []
    for name , times in student_times.items():
        final_times = max(times[1:])
        start_time = times[0]
        difference = final_times - start_time
        hours = difference.total_seconds() / 3600
        if hours > 3:
            cheated_students.append(name)
        
    return cheated_students

        



            
            

if __name__ == "__main__":
    print(cheaters())       


