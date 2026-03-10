# write your solution here
def matrix_sum():
    with open("matrix.txt") as new_file:
        matrix_sum = 0
        for ligne in new_file:
            ligne = ligne.replace("\n", "")
            list_numbers = ligne.split(",")
            for number in list_numbers:
                number = int(number)
                matrix_sum += number
        return matrix_sum 
def matrix_max():
    list_numbers = []
    with open("matrix.txt") as new_file:
        for ligne in new_file:
            ligne = ligne.replace("\n", "")
            list_ligne = ligne.split(",")
            for number in list_ligne:
                list_numbers.append(int(number))
        return max(list_numbers)
def row_sums():
    list_sums = []
    with open("matrix.txt") as new_file:
        for ligne in new_file:
            ligne = ligne.replace("\n", "")
            ligne = ligne.split(",")
            list_numbers = []
            for number in ligne:
                list_numbers.append(int(number))
            list_sums.append(sum(list_numbers))
    return list_sums


if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())