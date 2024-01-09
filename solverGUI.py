from tkinter import *


###############################variable_defining###################################
BACKGROUND = "#393F42"
ENTRYBOX_BG = "#E2FCFF"




###################################################################################

def printSudoku(arr): # function to print array
    for i in range(len(arr)):
        if i%3 == 0 :
            print("--------------------")
        for j in range(len(arr[i])):
            if j%3 == 0 :
                print("|", end="")
            print(arr[i][j], end=" ")
        print()

def findEmpty(arr): # function to find empty element in array
    EmpList=[]
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 0:
                EmpList.append((y,x))
    return EmpList

def IsValid(arr, pos, val):
    if val in arr[pos[0]]:
        return False
    elif val in [arr[i][pos[1]] for i in range(9)]:
        return False

    for i in range(3 * (pos[0] // 3), 3 + 3 * (pos[0] // 3)):
        for j in range(3 * (pos[1] // 3), 3 + 3 * (pos[1] // 3)):
            if val == arr[i][j]:
                return False
    return True


def solveSudoku(arr):
    EmpList = findEmpty(arr)
    if EmpList == []:
        return True
    else:
        for I in EmpList:
            for val in range(1,10):
                if IsValid(arr,I,val):
                    arr[I[0]][I[1]] = val
                    if solveSudoku(arr):
                        return True
                    arr[I[0]][I[1]] = 0
            return False            


######################################################### GUI part #################################################################

def initialArray(grid_entries):
    sudoku = [
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

    for row in range(9):
        for col in range(9):
            grid_val = grid_entries[row][col].get()
            if  grid_val is not None and grid_val.isdigit():
                sudoku[row][col] = int(grid_val)

    return sudoku

def createGrid(root):
    entries = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = Entry(root, width=2, font=('Helvetica', 35), bg=ENTRYBOX_BG)
            entry.grid(row=i, column=j, padx=2, pady=2)

            row_entries.append(entry)
        entries.append(row_entries)
    return entries

def main():
    global root
    root = Tk()
    root.title("Sudoku Solver")
    root.geometry("550x630")
    root.config(background=BACKGROUND)

    # Create a 9x9 grid of Entry widgets
    grid_entries = createGrid(root)
    
    # Add a Solve button (you can later add functionality to solve the puzzle)
    solve_button = Button(root, text="Solve", command=lambda :click(grid_entries), font=("consol",20))
    solve_button.grid(row=10, column=0, columnspan=15)

    root.mainloop()

def click(grid_entries):
    Sudoku = initialArray(grid_entries)
    solveSudoku(Sudoku)
    printSudoku(Sudoku)


if __name__ == "__main__":
    main()
