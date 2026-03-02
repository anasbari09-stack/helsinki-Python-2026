# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    seen = []                                       # for stock and check numbers if repeat
    for i in range(row_no, row_no + 3):             # loop with 3 rows start from the row give user 
        row = sudoku[i]                             
        for i in range(column_no, column_no + 3):   
            number = row[i]                         # number start from row and column give user 
            if number > 0:
                if number in seen:                  # if number we already stocks in seen return false because is repeat
                    return False
                seen.append(number)                 # add number to seen list after condition because if we add before return will give us False every time because we add number before check
    return True





if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))
