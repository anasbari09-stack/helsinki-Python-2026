from random import randint
def lottery_numbers(amount: int, lower: int, upper: int):
    clean_list = []
    while len(clean_list) < amount:         # the loop stop when he colected the amount of numbers
        new_random = randint(lower, upper)  # random number between lower and upper
        if new_random not in clean_list:    # add number to clean_list just if not in the list for don't have the same numbers in the list
            clean_list.append(new_random)
    return sorted(clean_list)               # i use sorted function to sorte values from smaller to bigger
