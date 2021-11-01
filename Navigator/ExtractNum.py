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
    for i in range(0,9):
        for j in range(0,3):
            for y in range(0,3):
                newqdLine.append(qdLine[i][j][y])
    
    newqdLineArray = np.array(newqdLine).reshape(9,9)

    return newqdLineArray

driver = navigator()
bs = driver.BeautifulSoup()

Allgrid = bs.findAll('div', attrs={'class':'game-grid__group'})
allNumbers = allTable(Allgrid)
tableResult = organizedTable(allNumbers)