from Shape import Shape
from ShapeRules import ShapeRules
from typing import List
from Cell import Cell


def horizontalLine(board:List[List[Cell]], lineNumber:int, rules:ShapeRules) -> Shape:
    shape = Shape(board[lineNumber], rules)
    for cell in board[lineNumber]:
        cell.inShapes.append(shape)
    return shape

def horizontalLines(board:List[List[Cell]], rules:ShapeRules) -> List[Shape]:
    cells = []
    for lineNumber in board:
        line = horizontalLine(board, lineNumber, rules)
        cells.append(line)
    return cells

def verticalLine(board:List[List[Cell]], lineNumber:int, rules:ShapeRules) -> Shape:
    shape = Shape([], rules)
    for horizontalLine in board:
        shape.cells.add(board[horizontalLine][lineNumber])
        board[horizontalLine][lineNumber].inShapes.append(shape)
    return shape

def verticalLines(board:List[List[Cell]], rules:ShapeRules) -> List[Shape]:
    lines = []
    for i in range(len(board)):
        lines.append(verticalLine(board, i, rules))
    return lines

def allLines(board:List[List[Cell]], rules:ShapeRules) -> List[Shape]:
    vertLines = verticalLines(board, rules)
    horLines = horizontalLines(board, rules)
    return vertLines + horLines
