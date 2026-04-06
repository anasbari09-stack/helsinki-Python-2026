# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1 = 0
    avg2 = 0
    avg3 = 0
    resulte = person1
    for key , value in person1.items():
        if key == "name":
            continue
        avg1 += value
    smallestAverage = avg1
    for key , value in person2.items():
        if key == "name":
            continue
        avg2 += value
    if avg2 < smallestAverage:
        smallestAverage = avg2
        resulte = person2
    for key , value in person3.items():
        if key == "name":
            continue
        avg3 += value
    if avg3 < smallestAverage:
        smallestAverage = avg3
        resulte = person3
    return resulte
    
