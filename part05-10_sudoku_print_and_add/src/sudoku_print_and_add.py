# Function to display the Sudoku grid nicely
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

# Function to update a specific cell in the grid
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    row = sudoku[row_no]  # Access the specific row (list) using the index
    row[column_no] = number  # Change the value at the specific column index
    # Note: Returning print_sudoku here makes the grid print every time you add a number.
    # In professional apps, we usually just update the data here.
    return print_sudoku(sudoku)   #you don't need return

        
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