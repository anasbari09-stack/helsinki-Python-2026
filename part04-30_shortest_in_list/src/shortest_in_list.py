# Write your solution here
def shortest(my_list):
    shortest = my_list[0]
    for i in range(0, len(my_list)):
        if len(my_list[i]) < len(shortest):
            shortest = my_list[i]
    return shortest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)