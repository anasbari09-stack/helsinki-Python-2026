# Write your solution here
def sum_of_positives(my_list):
    summe = 0
    for item in my_list:
        if item > 0:
            summe += item
    return summe

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
        
