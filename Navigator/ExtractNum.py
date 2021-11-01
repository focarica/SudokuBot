from wSelenium import WSelenium
from itertools import product
import numpy as np

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


quadrant = [alltable[0:9]]
for i in range(9,81,9):
    line = [alltable[i:i+9]]
    quadrant = np.append(quadrant, line, axis=0)

lineRange = range(0,9,3)

for index, l, c in product(lineRange,lineRange,lineRange):
    lines = quadrant[l:l+3, c:c+3]
    print(lines)