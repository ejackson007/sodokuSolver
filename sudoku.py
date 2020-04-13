#define a sodoku puzzle field
import numpy as np

#creating class that the table will hold. Using class to encapsulate value & markup
class sudokuSquare:
    def __init__(self):
        super().__init__()
        self.value = 0 #0 is not a valid option in sudoku, thus will be used as empty

        #Crook algorithm uses a markup to know possible values. In typical pencil
        #and paper method, you would write this in the bottom corner and then mark them out as they
        #become impossible. This program will make a list and then delete them
        self.markup = []

class sudokuTable:
    def __init__(self):
        super().__init__()
        #None is a place holder so that the space can be allocated. If
        #sudokuSquare is initialized instead of None, all objects will be
        #of the same instance
        self.puzzle = np.ndarray(shape=(9,9), dtype=sudokuSquare)
        #fill puzzle with squares
        for row in range(9):
            for col in range(9):
                self.puzzle[row][col] = sudokuSquare()

    def fillTable(self, table):
        for row in range(9):
            for col in range(9):
                self.puzzle[row][col].value = table[row][col]
        self.fillMarkup()

    def fillMarkup(self):
        #to fill mark up, you need to find all possible values that the square can be. You do this my comparing 3 tables, one of the surrounding 3x3 square,
        #one of the horizontal line, and one of the vertical line. After these 3 lists are made of all values, we can use combine them, and find the differences
        #with a list of all possible values to find which values should be in the markup
        allVal = [1,2,3,4,5,6,7,8,9]
        vertical = []
        horizontal = []
        surround = []

        for row in range(9):
            for col in range(9):
                #iterate through horizaontal and vertical lines if not filled
                if self.puzzle[row][col].value is 0:
                    for i in range(9):
                        #horizontal
                        if self.puzzle[row][i].value is not 0:
                            horizontal.append(self.puzzle[row][i].value)
                            #vertical
                        if self.puzzle[i][col].value is not 0:
                            vertical.append(self.puzzle[i][col].value)
                    #do all surrounding numbers (self contained 3x3)
                    #which row 3rd its in
                    if row/3 < 1:
                        rValue = 0
                    elif row/3 < 2 and row/3 >= 1:
                        rValue = 3#1st position
                    else:
                        rValue = 6
                    #which col 3rd is it in?
                    if col/3 < 1:
                        cValue = 0
                    elif col/3 < 2 and col/3 >= 1:
                        cValue = 3
                    else:
                        cValue = 6
                    #now that we the exact quadrant, we can fill the 3x3 surrounding grid
                    for r in range(3):
                        for c in range(3):
                            if self.puzzle[r + rValue][c + cValue].value is not 0:
                                surround.append(self.puzzle[r + rValue][c + cValue].value)
                    #combine all lists
                    combined = set().union(horizontal, vertical, surround)
                    #set markup to the possible values
                    self.puzzle[row][col].markup = list(set(allVal) - combined)
                    #empty lists
                    horizontal.clear()
                    vertical.clear()
                    surround.clear()

    def printTable(self):
        for row in self.puzzle:
            for square in row:
                print(square.value, end=" ") #dump values
            print() # new line for each row
    
    def printMarkupTable(self):
        for row in self.puzzle:
            for square in row:
                print(square.markup, end=" ") #dump values
            print() # new line for each row

check = [
   [2,9,5,7,0,0,8,6,0],
   [0,3,1,8,6,5,0,2,0],
   [8,0,6,0,0,0,0,0,0],
   [0,0,7,0,5,0,0,0,6],
   [0,0,0,3,8,7,0,0,0],
   [5,0,0,0,1,6,7,0,0],
   [0,0,0,5,0,0,1,0,9],
   [0,2,0,6,0,0,3,5,0],
   [0,5,4,0,0,8,6,7,2]
]

test = sudokuTable()
test.fillTable(check)
test.printTable()
test.printMarkupTable()

allVal = [1,2,3,4,5,6,7,8,9]
horizontal = [8,4,3,5]
vertical = [6,4,2,9,8]
surround = [7,6,8,4,3]

combined = set().union(horizontal, vertical, surround)
print(combined)
print(list(set(allVal) - combined))