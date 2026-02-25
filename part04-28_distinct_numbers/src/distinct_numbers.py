# Write your solution here
def distinct_numbers(my_list):
    new_list = []
    for i in range(0, len(my_list)):
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
    return sorted(new_list)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) 
