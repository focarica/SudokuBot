import numpy as np
from numpy import ndarray

class solverSudoku():
    def __init__(self, board: list):
        # Initialize the Sudoku solver with a 2D array (9x9) representing the board
        self.board = np.array(board).reshape(9,9)

    def isValid(self, board: list, num: int, position: tuple) -> bool:
        """
        Validates if a number can be placed at a given position (row, col).
        Checks row, column, and the 3x3 box.
        """
        
        # Check if the number exists in the row
        for i in range(len(board[0])):
            if board[position[0]][i] == num and position[1] != i:
                return False

        # Check if the number exists in the column
        for i in range(len(board)):
            if board[i][position[1]] == num and position[0] != i:
                return False

        # Check if the number exists in the 3x3 box
        box_x = position[1] // 3  # Column index of the box
        box_y = position[0] // 3  # Row index of the box

        # Iterate through the 3x3 box
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if board[i][j] == num and (i,j) != position:
                    return False

        # If no conflicts, the number is valid
        return True


    def findEmpty(self, board: list) -> tuple | None:
        """
        Finds an empty spot on the board (represented by 0).
        Returns a tuple (row, col) if an empty spot is found, None otherwise.
        """
        
        # Iterate through the board to find the first empty spot
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)  # Return the positionition of the empty spot

        # If no empty spots are found, return None
        return None


    def solve(self) -> bool:
        """
        Solves the Sudoku puzzle using backtracking.
        Returns True if the board is solved, False if no solution exists.
        """
        
        board = self.board
        
        # Find the next empty spot (represented by 0 on the board)
        find = self.findEmpty(board)
        
        if not find:
            # If there's no empty spot, the puzzle is solved
            return True
        else:
            # Unpack the position of the empty spot (row, col)
            row, col = find

        # Try digits 1 to 9 in the empty spot
        for i in range(1, 10):
            # Check if the number is isValid at the current positionition
            if self.isValid(board, i, (row, col)):
                # If isValid, place the number
                board[row][col] = i

                # Recursively attempt to solve the board with the new number
                if self.solve():
                    return True

                # If the current number doesn't lead to a solution, reset the spot (backtrack)
                board[row][col] = 0

        # If no number works, return False (backtrack)
        return False
    
    def getFinishedBoard(self) -> ndarray:
        """
        Returns the finished Sudoku board as a 9x9 numpy array.
        """
        
        board = self.board
        newBoard = []
        
        # Flatten the board into a 1D list for easy manipulation
        for i in range(len(board)):
            for j in range(len(board)):
                newBoard.append(board[i][j])

        # Reshape the list back into a 9x9 array
        newBoard = np.array(newBoard).reshape(9,9)

        return newBoard