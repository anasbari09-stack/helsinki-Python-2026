# Write your solution here
def oldest_person(people: list):
    oldest = people[0][1]
    name_old = people[0][0]
    for item in people:
        if item[1] < oldest:
            name_old = item[0]
            oldest = item[1]
    return name_old

if __name__ == "__main__":
    people_list = [('Emily', 2014), ('Arthur', 1977)]
    result = oldest_person(people_list)