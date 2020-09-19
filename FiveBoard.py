# Author: Clara Watson
# Date: September 18, 2020
# Description: a game of tik tak toe but on a larger scale

class FiveBoard:
    """creates an editable game of tiktak toe using loops and checks to find the winners"""
    def __init__(self):
        """initilizes the 2 private data members"""
        self._current_state = "UNFINISHED"
        self._list = [[ '-' for _ in range(15) ] for _ in range(15)]


    def get_current_state(self):
        """this checks to see what state the board is in and will tell you if x won, o won, the game is a draw, or if it is unfinished"""
        count = 0
        for x in range(15):
            count_x_row = 0
            count_x_col = 0 
            count_y_row = 0
            count_y_col = 0
            count_x_diag = 0
            count_y_diag = 0
            step = 0
            for y in range(15):
                if self._list[x][y] == "x":
                    count_x_row= count_x_row + 1
                if self._list[x][y] == "o":
                    count_y_row = count_y_row + 1
                if self._list[y][x] == "x":
                    count_x_col = count_x_col + 1
                if self._list[y][x] == "o":
                    count_y_col = count_y_col + 1
                if self._list[y+x][y+1] == "x":
                    count_x_diag = count_x_diag + 1
                if self._list[y+1][x+y] == "o":
                    count_y_diag = count_y_diag + 1
                if self._list[y][x] != "-":
                    count = count + 1
                if count_x_col > 5 or count_x_row > 5 or count_x_col > 5 or count_x_diag > 5:
                    self._current_state = "X_WON"
                elif count_x_col > 5 or count_y_row > 5 or count_y_col > 5 or count_y_diag > 5:
                    self._current_state = "O_WON"
                elif count == 225:
                    self._current_state = "DRAW"
                step = step + 1
        return self._current_state
    


    def make_move(self,row,col,val):
        """this function takes the move the user wants to make and iserts it onto the board"""
        if (self.get_current_state == "X_WON") or (self.get_current_state == "O_WON") or (self.get_current_state == "DRAW"):
            return False
        elif (self._list[row][col] != "-"):
            return False
        else:
            self._list[row][col] = val
            return True
        
    
    def print_board(self):
        """this prints the board so the user can see the game"""
        for x in range(15):
            print (' '.join(self._list[x]))


board = FiveBoard()
board.make_move(1, 2, 'x')
board.make_move(2, 3, 'x')
board.make_move(3, 4, 'x')
board.make_move(4, 5, 'x')
board.make_move(5, 6, 'x')
board.make_move(6, 7, 'x')

board.print_board()  # print the board
print(board.get_current_state())  # print the current state
