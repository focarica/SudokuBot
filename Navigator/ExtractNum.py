from wSelenium import navigator
from itertools import product
from solver import solverSudoku
import numpy as np

#Return all numbers from the table
def allTable(allGrid):
    numbers = []
    rangeAll = range(0,9)

    for index, row, column in product(rangeAll, rangeAll, rangeAll):
        attr = {
            'class':'game-grid__cell', 
            'data-row':f'{row}',
            'data-column':f'{column}'        
        }

        try:
            cell = allGrid[index].findChild('div', attrs=attr)
            number = cell.findChild('svg', attrs={'class','default'})

            if number != None:
                number = number.get_text().replace('\n',"")
            else:
                number = '0'
            
            numbers.append(int(number))
        except AttributeError:
            if (index+1) % 3 == 0:
                column = 0
            column += 1
        
    return numbers

#Organize numbers
def organizedTable(allNumbers):
    quadrant = [allNumbers[0:9]]
    qdLine, newqdLine = [], []

    #Split each line in quadrants
    for i in range(9,81,9):
        line = [allNumbers[i:i+9]]
        quadrant = np.append(quadrant, line, axis=0)
        
    #Extract lines from quadrant
    for row in range(0,9,3):
        for column in range(0,9,3):
            qdLine.append(quadrant[row:row+3, column:column+3])
    
    #Organize the lines
    for box in range(0,9):
        for row in range(0,3):
            for column in range(0,3):
                newqdLine.append(qdLine[box][row][column])
    
    newqdLineArray = np.array(newqdLine).reshape(9,9)

    return newqdLineArray

#Answer the table and organize to fill
def finishedTable(numbers):
    newBoard = []
    solver = solverSudoku(numbers)
    solver.solve()
    finishedBoard = solver.getFinishedBoard()

    #New lists with boxs
    for row in range(0,9,3):
        for column in range(0,9,3):
            newBoard.append(finishedBoard[row:row+3, column:column+3])
    
    newBoard = np.array(newBoard).reshape(9,9).tolist()

    return newBoard

nav = navigator()
bs = nav.BeautifulSoup()
driver = nav.GetDriver()

allGrid = bs.findAll('div', attrs={'class':'game-grid__group'})
allNumbers = allTable(allGrid)
tableResult = organizedTable(allNumbers)
finishedBoard = finishedTable(tableResult)

nav.FillCells(finishedBoard)