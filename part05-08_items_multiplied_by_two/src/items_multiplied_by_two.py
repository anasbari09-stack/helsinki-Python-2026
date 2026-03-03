# Write your solution here
def double_items(numbers: list):
    new_numbers = numbers[:]                # i did numbers[:] for new_numbers be just a copy and don't have same adress 
    for i in range(len(new_numbers)):       # if i change item in new_numbers not affect numbers list
        new_numbers[i] *= 2
    return new_numbers

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)