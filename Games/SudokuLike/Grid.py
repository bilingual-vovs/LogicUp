class Grid:
    def __init__(self, board:list, shapes:list, solved:list=None):
        self.initialBoard:list = board
        self.board:list = board
        self.shapes:list = shapes
        self.solved:list = solved

    # def solve(self):
    #     if self.solved:
    #         return self.solved
    #     #todo

    def reset(self):
        return self.initialBoard

    def insert(self, val, x, y):
        self.board[x][y].setTo(val)

    def isValid(self):
        for shape in self.shapes:
            if not shape.rules.isValid():
                return False
        return True
