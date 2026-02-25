# Write your solution here
def list_sum(list_1, list_2):
    list_sum = []
    for i in range(0, len(list_1)):
        list_sum.append(list_1[i] + list_2[i])
    return list_sum 

if __name__ == "__main__":
    list_1 = [1, 2, 3]
    list_2 = [7, 8, 9]
    print(list_sum(list_1, list_2))