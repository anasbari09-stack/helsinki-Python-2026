# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid_copy = []
    for item in sudoku:
        grid_copy.append(item[:])
    
    row = grid_copy[row_no]
    row[column_no] = number
    return grid_copy

if __name__ == "__main__":
    def print_sudoku(sudoku: list):
        attemps_r = 0  # Counter to keep track of rows (to print a space every 3 rows)
        for row in sudoku:  # Loop through each row in the 2D list
            attemps_c = 0  # Counter to keep track of columns (to print a space every 3 columns)
            for c in row:  # Loop through each individual cell/number in that row
                if attemps_c == 3:  # If we have printed 3 numbers...
                    print(" ", end="")  # Print an extra space for the vertical block border
                    attemps_c = 0  # Reset the column counter to start counting the next 3
                
                if c == 0:  # If the cell value is 0 (empty)...
                    print("_ ", end="")  # Print an underscore and a space
                else:  # If the cell has a number...
                    print(f"{c} ", end="")  # Print the number followed by a space
                
                attemps_c += 1  # Add 1 to the column counter after printing each cell
                
            attemps_r += 1  # Add 1 to the row counter after finishing a whole row
            if attemps_r == 3:  # If we have printed 3 rows...
                attemps_r = 0  # Reset the row counter
                print()  # Print one newline to finish the row
                print()  # Print a second newline to create the horizontal block gap
            else:  # If it's not the 3rd row...
                print()  # Just print one newline to go to the next line
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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
