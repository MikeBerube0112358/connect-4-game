import connect4

def main():
    #Make grid with user input
    try:
        nRows, nCols = map(int,input("Enter the number of rows and columns with a comma inbetween: ").split(','))
    except ValueError:
        print("Thanks for playing!")
        quit()
    if nRows < 4 or nRows > 10 or nCols < 4 or nCols > 10:
        print("Rows and columns must be between 4 and 10. ")
        quit()
    grid = connect4.makeGrid(nRows, nCols)

    #Start game 
    turn_counter = 1
    while turn_counter<1001:
        full_board(grid)
        
        if turn_counter%2!=0:
            column = int(input("Player red (X) pick the column you'd like to select: "))
        #Bad input check red
            try:
                connect4.play(grid, column, 'red')
            except IndexError:
                print('Invalid move')
                continue
        #Check for win red
            connect4.win(grid, column)
            print(connect4.toString(grid))
            turn_counter += 1
            if connect4.win(grid, column)=='red':
                print(f"Red wins after {turn_counter-1} moves!")
                quit()

        else:
            column = int(input("Player black (O) pick the column you'd like to select: "))
        #Bad input check black
            try:
                connect4.play(grid, column, 'black')
            except IndexError:
                print('Invalid move')
                continue
        #Check for win black
            connect4.win(grid, column)
            print(connect4.toString(grid))
            turn_counter += 1
            if connect4.win(grid, column)=='black':
                print(f"Black wins after {turn_counter-1} moves!")
                quit()
        #Check if board is full 
        full_board(grid)
        print(f'Move #{turn_counter-1}')



def full_board(grid):
    '''Checks if the board is full.'''
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='empty':
                count += 1
    if count==0:
        print(f"The game is a tie.")
        quit()
    return None


'''Main guard.'''
if __name__ == "__main__":
    main()