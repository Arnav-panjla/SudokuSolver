from tkinter import *
from tkinter import messagebox
import copy


###############################_Constants_Defining_###################################
GEOMETRY_ROOT = "750x600"
GEOMETRY_OUTPUT = "700x600"
BACKGROUND = "#393F42"
ENTRY_BG = "#E2FCFF"
ENTRY_FG = "blue"
LABEL_BG = "#E2FCFF"
LABEL_FG_IN = "blue"
LABEL_FG_OUT = "green"





########################################################_Sudoku_Solving_Algorithm_#############################################3

def printSudoku(arr): # function to print array(or more precisely Sudoku)
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
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == 0:
                EmpList.append((row,col))
    return EmpList

def IsValid(arr, pos, val): # finction to check of the given value is valid
    if val in arr[pos[0]]:
        return False
    elif val in [arr[i][pos[1]] for i in range(9)]:
        return False

    for i in range(3 * (pos[0] // 3), 3 + 3 * (pos[0] // 3)):
        for j in range(3 * (pos[1] // 3), 3 + 3 * (pos[1] // 3)):
            if val == arr[i][j]:
                return False
    return True


def solveSudoku(arr): # main algorithm to solve sudoku
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
        
#####################################################_Check_For_Error_##############################################################
        
def check(arr):
    empList = findEmpty(arr)
    for row in range(9):
        for col in range(9):
            if (row, col) not in empList:
                if IsValid(arr,(row, col), arr[row][col]):
                    pass
                else:
                    return False
    return True
                    



def problem(txt):
    messagebox.showerror(title="Invalid Sudoku", message=txt)
            




#########################################################_GUI_Part_#################################################################

def formSudoku(grid_entries):
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
            if  grid_val.isdigit():
                sudoku[row][col] = int(grid_val)

    return sudoku

def createGrid():
    entries = []

    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = Entry(root, width=2, font=('Helvetica', 35), bg=ENTRY_BG, fg=ENTRY_FG, justify='center')
            entry.grid(row=i, column=j, padx=2, pady=2)
            row_entries.append(entry)
        entries.append(row_entries)
    return entries


def displayResult(initialSudoku, finalSudoku): # function which displays output 
    out_window = Tk()
    out_window.geometry(GEOMETRY_OUTPUT)
    out_window.title("Sudoku Result Display")
    out_window.config(background=BACKGROUND)

    for i in range(9):
        for j in range(9):
            if initialSudoku[i][j] == 0:
                label = Label(out_window, text=str(finalSudoku[i][j]), width=2, height=1, font=('Helvetica', 30), background=LABEL_BG, fg=LABEL_FG_OUT)
                label.grid(row=i, column=j, padx=2, pady=2)
            else:
                label = Label(out_window, text=str(finalSudoku[i][j]), width=2, height=1, font=('Helvetica', 30), background=LABEL_BG, fg=LABEL_FG_IN)
                label.grid(row=i, column=j, padx=2, pady=2)


def clear():
    pass

def solve(grid_entries):
    initialSudoku = formSudoku(grid_entries) 
    finalSudoku = copy.deepcopy(initialSudoku)
    solveSudoku(finalSudoku)
    printSudoku(finalSudoku)
    root.destroy()
    displayResult(initialSudoku, finalSudoku)

    """
    if check(initialSudoku):
        finalSudoku = copy.deepcopy(initialSudoku)
        solveSudoku(finalSudoku)
        printSudoku(finalSudoku)
        root.destroy()
        displayResult(initialSudoku, finalSudoku)
    else:
        problem("There seems to be some problem with your Sudoku")
        del initialSudoku
    """

def main():
    global root
    root = Tk()
    root.title("Sudoku Solver")
    root.geometry(GEOMETRY_ROOT)
    root.config(background=BACKGROUND)

    # Create a 9x9 grid of Entry widgets
    grid_entries = createGrid()
    
    # Add a Solve button (you can later add functionality to solve the puzzle)
    solveButton = Button(master=root, text="   Solve   ", command=lambda :solve(grid_entries), font=('Consol', 20))
    solveButton.place(x=585,y=200)
    clearButton = Button(root, text=" Clear ", command=clear, font=('Consol', 20))
    clearButton.place(x=600, y=270)

    root.mainloop()


if __name__ == "__main__":
    main()
