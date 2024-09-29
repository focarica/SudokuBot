# Program flow in main file

## Step 1: Initialize the Navigator

```
navigator = Navigator()
```

Initializes the Navigator class, which handles:
- Launching the Selenium WebDriver
- Navigating to the Sudoku website
- Setting the desired difficulty level
- Managing interactions with the web page

## Step 2: Parse the Current Page Source with BeautifulSoup

```
bs = navigator.BeautifulSoup()
```

Uses BeautifulSoup to parse the current HTML page source.
This allows for easy extraction and manipulation of HTML elements.

## Step 3: Access the WebDriver Instance

```
driver = navigator.GetDriver()
```

Retrieves the Selenium WebDriver instance from the Navigator.

## Step 4: Locate the Sudoku Board on the Web Page

```
board = bs.findAll('div', attrs={'class': 'game-grid__group'})
```

Finds all HTML `<div>` elements with the class `game-grid__group`.
Each of these divs represents a 3x3 subgrid (quadrant) of the Sudoku board.
The `board` variable is a list containing these subgrid elements.

## Step 5: Extract Numbers from the Sudoku Board

```
allNumbers = allTable(board)
```

Calls the `allTable` function from the `ExtractNum` module.
- **Input:** `board` (list of BeautifulSoup elements representing each 3x3 quadrant)
- **Output:** `allNumbers` (a flat list of 81 integers representing the Sudoku board)

The `allTable` function iterates through each cell in the Sudoku grid,
extracting the number present or assigning `0` if the cell is empty.


## Step 6: Solve the Sudoku Puzzle

```
finishedBoard = finishedTable(allNumbers)
```

The `finishedTable` function:
1. Organizes the flat list into a structured 9x9 NumPy array.
2. Initializes the `solverSudoku` class with the organized board.
3. Attempts to solve the Sudoku puzzle using backtracking.
4. Retrieves the solved board and formats it for further use.

## Step 7: Fill the Solved Numbers Back into the Web Page

```
navigator.FillCells(finishedBoard)
```

The `FillCells` method performs the following:

1. Parses the current page source to identify which cells are already filled.
2. Determines the remaining numbers that need to be filled in each 3x3 quadrant.
3. Iterates through each empty cell and fills in the appropriate number.

This effectively updates the web-based Sudoku grid with the solved numbers.

