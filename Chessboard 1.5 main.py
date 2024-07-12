class Chessboard:
    def __init__(self):
        self.lista = [['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],
              ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
              ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],
              ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
              ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],
              ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
              ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],
              ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛']]

        self.object_chesspieces()
        self.display_board()


    def display_board(self):
        for row in self.lista:
            print(' '.join([piece.lista if isinstance(piece, Chesspiece) else piece for piece in row]))

    def object_chesspieces(self):
        self.lista[7][0] = Rook('♖ ', 'white', (3, 5))
        self.lista[7][7] = Rook('♖ ', 'white', (5, 5))
        self.lista[7][1] = Knight('♘ ', 'white', (7, 1))
        self.lista[7][6] = Knight('♘ ', 'white', (7, 6))
        self.lista[7][2] = Bishop('♗ ', 'white', (4, 4))
        self.lista[7][5] = Bishop('♗ ', 'white', (7, 5))
        self.lista[7][4] = Queen('♕ ', 'white', (7, 4))
        self.lista[7][3] = King('♔ ', 'white', (7, 3))
        for i in range(0, 8):
            self.lista[6][i] = Pawn('♙ ', 'white', (6, i))

        self.lista[0][0] = Rook('♜ ', 'black', (0, 0))
        self.lista[0][7] = Rook('♜ ', 'black', (4, 7))
        self.lista[0][1] = Knight('♞ ', 'black', (0, 1))
        self.lista[0][6] = Knight('♞ ', 'black', (0, 6))
        self.lista[0][2] = Bishop('♝ ', 'black', (0, 2))
        self.lista[0][5] = Bishop('♝ ', 'black', (0, 5))
        self.lista[0][4] = Queen('♛', 'black', (0, 4))
        self.lista[0][3] = King('♚ ', 'black', (0, 3))
        for i in range(0, 8):
            self.lista[1][i] = Pawn('♟ ', 'black', (1, i))


    def move_chessman(self):
        x1 = int(input("Enter the start position row of the chessman: "))
        y1 = int(input("Enter the start position column of the chessman: "))
        x2 = int(input("Enter the new position row: "))
        y2 = int(input("Enter the new position column: "))
        if 0 <= x1 < 8 and 0 <= y1 < 8:
            piece = self.lista[x1][y1]
            if 0 <= x2 < 8 and 0 <= y2 < 8:
                piece.move(self,x1,y1, x2, y2)
                self.display_board()
            else:
                print("New position out of bounds")
        else:
            print("Start position out of bounds")



class Chesspiece:
    def __init__(self,lista,color,position):
        self.lista = lista
        self.color = color
        self.position = position

    @staticmethod
    def replace_color(x1, y1):
        if (x1 + y1) % 2 == 0:
            return '⬛'
        else:
            return '⬜'



class Pawn(Chesspiece):
    def __init__(self, lista, color, position):
        super().__init__(lista, color, position)
    def move(self, chessboard, x1, y1, x2, y2):
        direction = 1 if self.color == 'black' else -1
        initial_row = 1 if self.color == 'black' else 6
        distance = x2 - x1 if self.color == 'black' else x1 - x2
        if y1 == y2:
            if isinstance(chessboard.lista[x2][y2], str):
                chessboard.lista[x2][y2] = chessboard.lista[x1][y1]
                chessboard.lista[x1][y1] = Chesspiece.replace_color(x1, y1)
                self.position = (x2, y2)
                return True
            else:
                print("The move is`t possible")
                return False
        elif abs(y2 - y1) == 1 and distance == 1:
            if not isinstance(chessboard.lista[x2][y2], str) and self.color != chessboard.lista[x2][y2].color:
                chessboard.lista[x2][y2] = chessboard.lista[x1][y1]
                chessboard.lista[x1][y1] = Chesspiece.replace_color(x1, y1)
                self.position = (x2, y2)
                return True
            else:
                print("The cell is occupied by a chesspiece of your color")
                return False
        else:
            print("Invalid move")
            return False


class Rook(Chesspiece):
    def __init__(self, lista, color, position):
        super().__init__(lista, color, position)

    def move(self, chessboard, x1, y1, x2, y2):
            if x1 == x2 or y1 == y2:
                if self.is_route_clear_rook(chessboard, x1, y1, x2, y2):
                    if isinstance(chessboard.lista[x2][y2], str) or (chessboard.lista[x1][y1].color != chessboard.lista[x2][y2].color):
                        chessboard.lista[x2][y2] = chessboard.lista[x1][y1]
                        chessboard.lista[x1][y1] = Chesspiece.replace_color(x1, y1)
                        self.position = (x2, y2)
                        return True
                    else:
                        print("The cell is occupied by a chesspiece of your color")
                else:
                    return False
            else:
                print("Invalid move")
            return False

    def is_route_clear_rook(self, chessboard, x1, y1, x2, y2):
        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for i in range(y1 + step, y2, step):
                if not isinstance(chessboard.lista[x1][i], str):
                    print("The move is`t possible")
                    return False
        elif y1 == y2:
            step = 1 if x2 > x1 else -1
            for i in range(x1 + step, x2, step):
                if not isinstance(chessboard.lista[i][y1], str):
                    print("The move is`t possible")
                    return False
        return True


class Bishop(Chesspiece):
    def __init__(self, lista, color, position):
        super().__init__(lista, color, position)
    def move(self, chessboard,  x1, y1, x2, y2):
        if abs(x1 - x2) == abs(y1 - y2):
                if self.is_route_clear_bishop(chessboard, x1, y1, x2, y2):
                    if isinstance(chessboard.lista[x2][y2], str) or (chessboard.lista[x1][y1].color != chessboard.lista[x2][y2].color):
                        chessboard.lista[x2][y2] = chessboard.lista[x1][y1]
                        chessboard.lista[x1][y1] = Chesspiece.replace_color(x1, y1)
                        self.position = (x2, y2)
                        return True
                    else:
                        print("The cell is occupied by a chesspiece of your color")
                else:
                    return False
        else:
            print("Invalid")

    def is_route_clear_bishop(self, chessboard, x1, y1, x2, y2):
        step_x = 1 if x2 > x1 else -1
        step_y = 1 if y2 > y1 else -1
        i = x1 + step_x
        j =  y1 + step_y
        while i != x2 or j != y2:
            if not isinstance(chessboard.lista[i][j], str):
                print("The move is`t possible")
                return False
            i += step_x
            j += step_y
        return True



class Knight(Chesspiece):
    def __init__(self, lista, color, position):
        super().__init__(lista, color, position)
    def move(self, chessboard,  x1, y1, x2, y2):
        if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
            if isinstance(chessboard.lista[x2][y2], str) or (chessboard.lista[x1][y1].color != chessboard.lista[x2][y2].color):
                chessboard.lista[x2][y2] = chessboard.lista[x1][y1]
                chessboard.lista[x1][y1] = Chesspiece.replace_color(x1, y1)
                self.position = (x2, y2)
                return True
            else:
                print("The cell is occupied by a chesspiece of your color")
        else:
            print("Invalid")

class Queen(Chesspiece):
    def __init__(self, lista, color, position):
        super().__init__(lista, color, position)
    def move(self, chessboard,  x1, y1, x2, y2):
        if (abs(x1 - x2) == abs(y1 - y2)) or x1 == x2 or y1 == y2:
                if self.is_route_clear_queen(chessboard,  x1, y1, x2, y2):
                    if isinstance(chessboard.lista[x2][y2], str) or (chessboard.lista[x1][y1].color != chessboard.lista[x2][y2].color):
                        chessboard.lista[x2][y2] = chessboard.lista[x1][y1]
                        chessboard.lista[x1][y1] = Chesspiece.replace_color(x1, y1)
                        self.position = (x2, y2)
                        return True
                    else:
                        print("The cell is occupied by a chesspiece of your color")
                else:
                    return False
        else:
            print("Invalid")

    def is_route_clear_queen(self, chessboard,  x1, y1, x2, y2):
        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for i in range(y1 + step, y2, step):
                if not isinstance(chessboard.lista[x1][i], str):
                    print("The move is`t possible")
                    return False
        elif y1 == y2:
            step = 1 if x2 > x1 else -1
            for i in range(x1 + step, x2, step):
                if not isinstance(chessboard.lista[i][y1], str):
                    print("The move is`t possible")
                    return False
        elif abs(x1 - x2) == abs(y1 - y2):
            step_x = 1 if x2 > x1 else -1
            step_y = 1 if y2 > y1 else -1
            i = x1 + step_x
            j = y1 + step_y
            while i != x2 or j != y2:
                if not isinstance(chessboard.lista[i][j], str):
                    print("The move is`t possible")
                    return False
                i += step_x
                j += step_y
        return True



class King(Chesspiece):
    def __init__(self, lista, color, position):
        super().__init__(lista, color, position)
    def move(self, chessboard, x1, y1, x2, y2):
            if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
                if isinstance(chessboard.lista[x2][y2], str) or (chessboard.lista[x1][y1].color != chessboard.lista[x2][y2].color):
                    chessboard.lista[x2][y2] = chessboard.lista[x1][y1]
                    chessboard.lista[x1][y1] = Chesspiece.replace_color(x1, y1)
                    self.position = (x2, y2)
                    return True
                else:
                    print("The cell is occupied by a chesspiece of your color")
            else:
                print("Invalid")
                return False


chessboard = Chessboard()
chessboard.move_chessman()


















