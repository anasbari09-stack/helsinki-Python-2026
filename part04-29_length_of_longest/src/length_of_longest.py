# Write your solution here
def length_of_longest(my_list):
    long_string = my_list[0]
    for i in range(0, len(my_list)):
        if len(my_list[i]) > len(long_string):
            long_string = my_list[i]
    return len(long_string)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)