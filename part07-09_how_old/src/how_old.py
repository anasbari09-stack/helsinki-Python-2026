from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

Millennium_day = datetime(1999, 12, 31)
birth_day = datetime(year, month, day)
difference = Millennium_day - birth_day

if difference.days > 0:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")