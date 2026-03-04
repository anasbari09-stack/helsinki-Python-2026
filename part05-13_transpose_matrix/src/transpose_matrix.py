# Write your solution here
def transpose(matrix: list):
    copy_list = []
    for item in matrix:
        copy_list.append(item[:])
    for c in range(0, len(matrix)):
        for r in range(0, len(matrix)):
            
            matrix[r][c] = copy_list[c][r]
    


if __name__ == "__main__":
    my_list = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
    print(transpose(my_list))