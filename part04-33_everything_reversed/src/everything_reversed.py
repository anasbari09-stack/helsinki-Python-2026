# Write your solution here
# Write your solution here
def everything_reversed(my_list):
    reversed_list = my_list[::-1]
    new_list = []
    for item in reversed_list:
        new_list.append(item[::-1])
    return new_list
    
if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)