# Write your solution here
from datetime import datetime
def final_points():
    students = {}
    with open("start_times.csv") as f:
        for line in f:
            name, start_time = line.strip().split(";")
            students[name] = {}
            students[name]['start time'] = datetime.strptime(start_time, "%H:%M")
    
    with open("submissions.csv") as file:
        for line in file:
            name, task, points, submission_time = line.strip().split(";")
            points = int(points)
            submission_time = datetime.strptime(submission_time, "%H:%M")
            diffirence = submission_time - students[name]['start time']
            if name in students and diffirence.total_seconds() <= 3 * 3600:
                if 'tasks' not in students[name]:
                    students[name]['tasks'] = {}
                tasks = students[name]['tasks']
                if task not in tasks or points > tasks[task]:
                    tasks[task] = points
    final_pts = {}
    for name , dic in students.items():
        final_pts[name] = sum(dic['tasks'].values())
    return final_pts
            


if __name__ == "__main__":
    final_points()
