
# array = arr[row][column]

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

def main():
    print("Initial sudoku matrix")
    printSudoku(sudoku)
    isComp = solveSudoku(sudoku)
    if isComp:
        print("\n")
        print("Final sudoku matrix -->")
        printSudoku(sudoku)
    else:
        print("Sorry! your sudoku is not solvable :(")


if __name__ == "__main__":
    main()