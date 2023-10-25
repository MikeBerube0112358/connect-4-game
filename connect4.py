
'''Makes grid using lists thats capped at 4 <= n <= 10.'''
def makeGrid(nRows, nCols):
    '''Makes grid using lists thats capped at 4 <= n <= 10.'''
    if nRows < 4 or nRows > 10 or nCols < 4 or nCols > 10:
        print("Rows and columns must be between 4 and 10. ")
        quit()
    grid = []
    for i in range(nRows): 
        grid.append([])
        for _ in range(nCols):
            grid[i].append('empty')
    return grid



def play(grid, column, checker):
    '''Puts checker at first avaiable position in column red or black.'''
    for i in range(1,len(grid)+1):
        if grid[len(grid)-i][column] == 'empty':
            grid[len(grid)-i][column] = checker
            return True
    return False



def win(grid, column):
    '''Checks for horizontal, vertical and diagonal wins.'''
    count, count2, hcount, hcount2, dcount, dcount2 = 0, 0, 0, 0, 0, 0
    rows, cols = len(grid), len(grid[0])

    # Vertical win for red and black
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'red':
                count += 1
                if count == 4:
                    return 'red'
            else:
                count = 0

            if grid[i][j] == 'black':
                count2 += 1
                if count2 == 4:
                    return 'black'
            else:
                count2 = 0

    # Horizontal win for red and black
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'red':
                hcount += 1
                if hcount == 4:
                    return 'red'
            else:
                hcount = 0

            if grid[i][j] == 'black':
                hcount2 += 1
                if hcount2 == 4:
                    return 'black'
            else:
                hcount2 = 0

    # Diagonal win from top-left to bottom-right
    for i in range(rows - 3):
        for j in range(cols - 3):
            if grid[i][j] == grid[i + 1][j + 1] == grid[i + 2][j + 2] == grid[i + 3][j + 3]:
                if grid[i][j] == 'red':
                    return 'red'
                elif grid[i][j] == 'black':
                    return 'black'

    # Diagonal win from top-right to bottom-left
    for i in range(rows - 3):
        for j in range(3, cols):
            if grid[i][j] == grid[i + 1][j - 1] == grid[i + 2][j - 2] == grid[i + 3][j - 3]:
                if grid[i][j] == 'red':
                    return 'red'
                elif grid[i][j] == 'black':
                    return 'black'

    return 'empty'


def toString(grid):
    '''Uses grid to make connect4 board.'''
    board = ''
    for i in range(len(grid)):
        board += '|'
        for j in range(len(grid[0])):
            if grid[i][j]=='empty':
                board += ' '
            elif grid[i][j]=='red':
                board += 'X'
            elif grid[i][j]=='black':
                board += 'O'
        board += f'|{i}\n'
    board += f'+{len(grid[0])*"-"}+'
    board += f'\n '
    for k in range(len(grid[0])):
        board += f'{k}'
    return board