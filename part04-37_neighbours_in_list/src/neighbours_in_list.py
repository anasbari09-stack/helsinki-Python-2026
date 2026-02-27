def longest_series_of_neighbours(my_list):
    length = 0
    big_length = 0
    for i in range(1, len(my_list)):
        if my_list[i] + 1 == my_list[i -1] or my_list[i - 1] + 1 == my_list[i]:
            if length == 0:
                length += 2
            else:
                length += 1
            if length > big_length:
                big_length = length
        else:
            length = 0
    return big_length

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))