# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
names = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2]
notes = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum_note = 0
        for note in parts[1:]:
            sum_note += int(note)
        notes[parts[0]] = sum_note
for ident , name in names.items():
    if ident in notes:
        sum_notes = notes[ident]
        print(f"{name} {sum_notes}") 
    
