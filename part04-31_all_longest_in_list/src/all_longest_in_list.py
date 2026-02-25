# Write your solution here
def all_the_longest(my_list):
    longest_string = []
    long_string = my_list[0]
    for i in range(0, len(my_list)):
       
        if len(my_list[i]) == len(long_string):
            longest_string.append(my_list[i])
        elif len(my_list[i]) > len(long_string):
            longest_string = []
            longest_string.append(my_list[i])

        if len(long_string) < len(my_list[i]):
            long_string = my_list[i]
    return longest_string

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) 
        
