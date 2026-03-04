# Write your solution here
def times_ten(start_index: int, end_index: int):
    numbers_dic = {}
    for i in range(start_index , end_index + 1):
        numbers_dic[i] = i * 10
    return numbers_dic

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)