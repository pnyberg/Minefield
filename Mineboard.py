from random import randint
from Node import Node

class Mineboard:
    def __init__(self, column, row, numberOfMines):
        self.nodes = []
        self.numberOfMines = numberOfMines

        self.createMines(column, row, numberOfMines)

    def createMines(self, column, row, numberOfMines):
        for x in range(column):
            nodeRow = []
            for y in range(row):
                nodeRow.append(Node())
            self.nodes.append(nodeRow)

        i = 0
        while (i < numberOfMines):
            x = randint(0, column - 1)
            y = randint(0, row - 1)

            if self.nodes[x][y].type == 0:
                self.nodes[x][y].setType(-1)
                i += 1

        for x in range(len(self.nodes)):
            for y in range(len(self.nodes[x])):
                if self.nodes[x][y].type != -1:
                    self.nodes[x][y].setType(self.getNeighbours(x, y))

    def getNeighbours(self, column, row):
        neighbours = 0

        for x in range(column - 1, column + 2):
            if x < 0 or x >= len(self.nodes):
                continue
            for y in range(row - 1, row + 2):
                if y < 0 or y >= len(self.nodes):
                    continue
                if x == column and y == row:
                    continue
                if self.nodes[x][y].type == -1:
                    neighbours += 1
        return neighbours

    def open(self, column, row):
        if self.nodes[column][row].open or self.nodes[column][row].mark:
            return
        if self.nodes[column][row].openNode():
            self.openSurroundings(column, row)

    def mark(self, column, row):
        if self.nodes[column][row].open:
            return
        self.nodes[column][row].fixMark()

    def openSurroundings(self, column, row):
        for x in range(column - 1, column + 2):
            if x < 0 or x >= len(self.nodes):
                continue
            for y in range(row - 1, row + 2):
                if y < 0 or y >= len(self.nodes):
                    continue
                self.open(x,y)

    def checkBoard(self):
        for x in range(len(self.nodes)):
            for y in range(len(self.nodes[x])):
                if not self.nodes[x][y].open and not self.nodes[x][y].mark:
                    return False
        return True
