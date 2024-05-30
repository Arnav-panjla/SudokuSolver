from tkinter import *
from tkinter import messagebox
import time

###################################################_Constants_Defining_#############################################

GEOMETRY_ROOT = "750x600"
BACKGROUND = "#393F42"
ENTRY_BG = "#E2FCFF"
ENTRY_FG = "blue"
LABEL_BG = "#E2FCFF"
LABEL_FG = "green"
TITLE_COLOR = "white"
SPEED = 220
########################################################_Sudoku_Solving_Algorithm_#############################################3


def findEmpty(arr): # function to find empty element in array (in this case sudoku ) and also adds label box to the filled element
    EmpList=[]
    for row in range(9):
        for col in range(9):
            if arr[row][col] not in range(1,10):
                EmpList.append((row,col))

    return EmpList


def IsValidMove(arr, pos, val): # function to check of the given value is valid
    
    if val in arr[pos[0]]:
        return False
    elif val in [arr[i][pos[1]] for i in range(9)]:
        return False

    for i in range(3 * (pos[0] // 3), 3 + 3 * (pos[0] // 3)):
        for j in range(3 * (pos[1] // 3), 3 + 3 * (pos[1] // 3)):
            if val == arr[i][j]:
                return False
    return True


def solveSudoku(arr, delay, num=0): # main algorithm to solve sudoku
    EmpList = findEmpty(arr)
    if EmpList == []:
        updateBoard(arr)
        return True
    else:
        for I in EmpList: # I[0] is row I[1] is column
            for val in range(1,10):
                if IsValidMove(arr,I,val):
                    arr[I[0]][I[1]] = val
                    if solveSudoku(arr, delay, num):
                        return True
                    arr[I[0]][I[1]] = ' '
                    num+=1
                    if num >= delay:
                        updateBoard(arr)
                        num=0
            return False     
      
        

#####################################################_Check_For_Error_##############################################################
        

def isValidSudoku(sud):
    for row in range(9):
        for col in range(9):
            val = sud[row][col]
            if  val in range(1,10):
                sud[row][col] = ' '
                if not IsValidMove(sud, (row, col), val):
                    txt = f"row:{row+1} col:{col+1} seems to be invalid. "
                    print(txt)
                    problem(txt)
                    return False
                else:
                    sud[row][col] = val
            elif val in [""," ", "  "]:
                pass
            else:
                txt = f"Invalid entry at row:{row+1} col:{col+1} "
                print(txt)
                problem(txt)
                return False

    return True
                    

def problem(txt):
    messagebox.showerror(title="Invalid Sudoku", message=txt)
            

#########################################################_GUI_Part_#################################################################


def formSudoku(grid_entries):
    sudoku = [[' ' for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            grid_val = grid_entries[row][col].get()
            if grid_val.isdigit():
                sudoku[row][col] = int(grid_val)
            else:
                sudoku[row][col] = grid_val
    return sudoku


def createGrid():
    entries = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = Entry(root, width=2, font=('Helvetica', 32), bg=ENTRY_BG, fg=ENTRY_FG, justify='center')
            entry.grid(row=i+2, column=j+2, padx=2, pady=2)
            entry.bind("<KeyPress>", lambda event, row=i, col=j: keyPress(event, row, col))
            row_entries.append(entry)
        entries.append(row_entries)
    return entries


def keyPress(event, row, col):
    if event.keysym == 'Up':
        moveFocus(row, col, -1, 0)
    elif event.keysym == 'Down':
        moveFocus(row, col, 1, 0)
    elif event.keysym == 'Left':
        moveFocus(row, col, 0, -1)
    elif event.keysym == 'Right':
        moveFocus(row, col, 0, 1)


def moveFocus(row, col, row_inc, col_inc):
    new_row = (row + row_inc) % 9
    new_col = (col + col_inc) % 9
    grid_entries[new_row][new_col].focus_set()


def addVal(row, col, val): # this function will add the value to a particular row and col
    Label(root, text=str(val), width=2, height=1, font=('Helvetica', 30), background=LABEL_BG, fg=LABEL_FG).grid(row=row+2, column=col+2, padx=2, pady=2)
    root.update()


def updateBoard(board):
    for row in range(9):
        for col in range(9):
            if (row, col) not in initialEntry:
                addVal(row, col, board[row][col])


def solve(grid_entries, delay):
    # check if the given sudoku is valid or not
    finalSudoku = formSudoku(grid_entries) 

    if isValidSudoku(finalSudoku):
        global initialEntry
        initialEntry = []
        # to convert filled entry to label
        for row in range(9):
            for col in range(9):
                val = grid_entries[row][col].get()
                if val.isdigit():
                    initialEntry.append((row, col))
                    Label(root, text=str(val), width=2, height=1, font=('Helvetica', 30), background=LABEL_BG, fg=ENTRY_FG).grid(row=row+2, column=col+2, padx=2, pady=2)
        # sudoku solving function
        solveSudoku(finalSudoku, delay)
    else:
        start()


def start():
    global grid_entries
    #create a 9x9 grid of entry boxes
    grid_entries = createGrid()

    solveButton = Button(master=root, text="   Solve   ", command=lambda: solve(grid_entries, SPEED), font=('Consol', 20))
    solveButton.place(x=585, y=180)
    fastSolveButton = Button(master=root, text="Fast Solve", command=lambda: solve(grid_entries, 50), font=('Consol', 20))
    fastSolveButton.place(x=575, y=250)
    clearButton = Button(root, text=" Clear ", command=start, font=('Consol', 20))
    clearButton.place(x=600, y=320)


def main():
    global root
    root = Tk()
    root.title("Sudoku Solver")
    root.geometry(GEOMETRY_ROOT)
    root.config(background=BACKGROUND)
    Label(root, text="SUDOKU SOLVER" ,font=('Helvetica', 30), background=BACKGROUND, foreground=TITLE_COLOR).grid(row=0, column=1, columnspan=10)
    Label(root, text=" " ,font=('Helvetica', 20), background=BACKGROUND, foreground=TITLE_COLOR).grid(row=0, column=0)

    start()

    root.mainloop()


if __name__ == "__main__":
    main()
