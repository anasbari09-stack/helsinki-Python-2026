# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for square in row:
        if square > 0:
            count = row.count(square)
            if count > 1:
                return False
    return True

def column_correct(sudoku: list, column_no: int):
    column_list = []
    for row in sudoku:
        column_list.append(row[column_no])
    for square in column_list:
        if square > 0:
            count = column_list.count(square)
            if count > 1:
                return False
    return True
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

def sudoku_grid_correct(sudoku: list):
    for i in range(0, len(sudoku)):
        if row_correct(sudoku, i) is False:
            return False
        if column_correct(sudoku, i) is False:
            return False
    for r in range(0, len(sudoku), 3):
        for c in range(0, len(sudoku), 3):
            if block_correct(sudoku, r, c) is False:
                return False
    return True

if __name__ == "__main__":
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))          
                
            


