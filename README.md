# Sudoku Solver

This is a simple Sudoku solver implemented in Python. The solver uses a backtracking algorithm to find the solution for the given Sudoku puzzle.

## Sudoku Representation

The Sudoku puzzle is represented as a 9x9 matrix in the code. Zeros in the matrix represent empty cells, and non-zero values represent initial values in the puzzle.

python
sudoku = [
    [0, 2, 0, 0, 5, 0, 8, 0, 0],
    [4, 0, 0, 0, 1, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [6, 0, 5, 0, 0, 7, 1, 0, 0],
    [0, 3, 4, 0, 2, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [3, 0, 0, 0, 7, 0, 0, 1, 5],
    [1, 0, 0, 0, 4, 0, 0, 0, 3],
    [0, 6, 0, 0, 0, 0, 0, 2, 0]
]
## Functions
# printSudoku(arr)
Prints the Sudoku matrix in a readable format. It includes horizontal and vertical dividers to represent the 3x3 subgrids.

# findEmpty(arr)
Finds and returns a list of coordinates for empty cells (zeros) in the Sudoku matrix.

# IsValid(arr, pos, val)
Checks if placing a certain value (val) at a given position (pos) in the Sudoku matrix is a valid move according to Sudoku rules.

# solveSudoku(arr)
Recursively solves the Sudoku puzzle using backtracking. It returns True if a solution is found, and False if the puzzle is not solvable.

# main()
Prints the initial Sudoku matrix, attempts to solve the puzzle, and prints the final solved matrix or a message indicating that the Sudoku is not solvable.

# Usage
Modify the sudoku matrix with your Sudoku puzzle.
Run the script.