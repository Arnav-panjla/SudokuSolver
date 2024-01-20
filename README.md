# Sudoku Solver

This Python script provides a simple GUI-based Sudoku solver using the Tkinter library. The solver uses a backtracking algorithm to fill in the missing numbers in a partially filled Sudoku grid.

## Table of Contents
- [Constants](#constants)
- [Sudoku Solving Algorithm](#sudoku-solving-algorithm)
- [Check for Errors](#check-for-errors)
- [GUI Part](#gui-part)

## Constants

<br>GEOMETRY_ROOT = "750x600"
<br>BACKGROUND = "#393F42"
<br>ENTRY_BG = "#E2FCFF"
<br>ENTRY_FG = "blue"
<br>LABEL_BG = "#E2FCFF"
<br>LABEL_FG = "green"
<br>TITLE_COLOR = "white"
<br>SPEED = 0.02

<br>GEOMETRY_ROOT: Initial size of the GUI window.
<br>BACKGROUND: Background color of the GUI.
<br>ENTRY_BG, ENTRY_FG: Background and foreground colors for entry boxes.
<br>LABEL_BG, LABEL_FG: Background and foreground colors for labels.
<br>TITLE_COLOR: Color of the title text.
<br>SPEED: Delay between steps in the Sudoku solving animation.

## Sudoku Solving Algorithm
The Sudoku solving algorithm includes functions for finding empty cells, validating moves, and solving the puzzle using backtracking.

## Check for Errors
The script includes a function to check if the input Sudoku puzzle is valid.

## GUI Part
The GUI section includes functions for creating the Sudoku grid, adding values to the grid, and providing buttons for solving and clearing the puzzle.