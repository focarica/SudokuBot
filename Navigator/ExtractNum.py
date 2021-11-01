from wSelenium import WSelenium
from itertools import product
import string
import numpy as np

#Return all numbers from the table
def allTable(grid):
    numbers = []
    rangeAll = range(0,9)

    for index, row, column in product(rangeAll, rangeAll, rangeAll):
        attr = {
            'class':'game-grid__cell', 
            'data-row':f'{row}',
            'data-column':f'{column}'        
        }

        try:
            cell = grid[index].findChild('div', attrs=attr)
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

driver = WSelenium()
bs = driver.BeautifulSoup()

Allgrid = bs.findAll('div', attrs={'class':'game-grid__group'})
alltable = allTable(Allgrid)

#Split each line in quadrants
quadrant = [alltable[0:9]]
for i in range(9,81,9):
    line = [alltable[i:i+9]]
    quadrant = np.append(quadrant, line, axis=0)

qd = []
newqd = []

#Extract lines from quadrant
for c in range(0,9,3):
    for l in range(0,9,3):
        qd.append(quadrant[c:c+3, l:l+3])

#Organize the lines
for i in range(0,9):
    for j in range(0,3):
        for y in range(0,3):
            newqd.append(qd[i][j][y])

for i in np.array_split(newqd, 9):
    print(list(i))