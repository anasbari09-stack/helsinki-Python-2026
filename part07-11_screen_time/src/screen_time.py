# Write your solution here
from datetime import datetime, timedelta
file_name = input("Filename: ")
with open(file_name, "w") as f:
    pass
starting_date = input("Starting date: ")
days = int(input("How many days: "))
parts_date = starting_date.split(".")
day = int(parts_date[0])
date = datetime(int(parts_date[2]),int(parts_date[1]),day)
starting_date = date
final_date = date + timedelta(days = days-1)
print("Please type in screen time in minutes on each day (TV computer mobile):")
total_minutes = 0
date_time = {}
for i in range(days):
    screen_time = input(f"Screen time {date.strftime("%d.%m.%Y")}: ")
    parts_time = screen_time.split(" ")
    total_minutes += int(parts_time[0]) + int(parts_time[1]) + int(parts_time[2])
    date_time[date.strftime("%d.%m.%Y")] = f"{parts_time[0]}/{parts_time[1]}/{parts_time[2]}"
    date += timedelta(days = 1)
average_minutes = total_minutes / days
print(f"Data stored in file {file_name}")
starting_date = starting_date.strftime("%d.%m.%Y")
with open(file_name, "a") as f:
    f.write(f"Time period: {starting_date}-{final_date.strftime("%d.%m.%Y")}\n")
    f.write(f"Total minutes: {total_minutes}\n")
    f.write(f"Average minutes: {average_minutes}\n")

    for date , time in date_time.items():
        f.write(f"{date}: {time}\n")


    
