# Write your solution here
def print_sudoku(sudoku: list):
    attemps_r = 0
    for row in sudoku:
        attemps_c = 0
        for c in row:
            if attemps_c == 3:
                print(" ", end="")
                attemps_c = 0
            if c == 0:
                print("_ ", end="")
            else:
                print(f"{c} ", end="")
            attemps_c += 1
        attemps_r += 1
        if attemps_r == 3:
            attemps_r = 0
            print()
            print()
            
        else:
            print()
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    row = sudoku[row_no]
    row[column_no] = number
    return print_sudoku(sudoku)

        
if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)