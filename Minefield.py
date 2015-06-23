# -- coding: utf-8 --
# requires: python tkinter

# TODO: fixa tidräknare
# TODO: manuellt ställa in rader, kolumner och minor
# TODO: fixa vinst/förlust-label

from tkinter import *
from Mineboard import Mineboard
from math import *

class Minefield:
	def __init__(self, master):
		self.numberOfMines = 10
		self.numberOfRows = 10
		self.numberOfColumns = 10
		self.boardAdjustmentX = 20
		self.boardAdjustmentY = 20
		self.cellHeight = 30
		self.cellWidth = 30

		self.game = True
		self.master = master
		self.frame = Frame(master)
		self.board = Mineboard(self.numberOfColumns, self.numberOfRows, self.numberOfMines)

		self.frame.pack( expand = YES, fill = BOTH )
		self.frame.master.title( "Demonstrating Mouse Events" )
		self.frame.master.geometry(  str(self.boardAdjustmentX * 2 + self.numberOfColumns * self.cellWidth) + "x" + str(self.boardAdjustmentY * 2 + self.numberOfRows * self.cellHeight) )
		self.canvas = Canvas(self.frame, width = self.boardAdjustmentX + 1 + self.numberOfColumns * self.cellWidth, height = self.boardAdjustmentY + 1 + self.numberOfRows * self.cellHeight)
		self.canvas.grid(row=0, column=0, sticky=N+S+E+W)

		self.update()

		self.canvas.bind( "<ButtonRelease-1>", self.openCell )   
		self.canvas.bind( "<ButtonRelease-3>", self.markCell )   

	def openCell( self, event ):
		if not self.game:
			return

		x = floor((event.x - 2 - self.boardAdjustmentX) / self.cellWidth)
		y = floor((event.y - 3 - self.boardAdjustmentY) / self.cellHeight)

		if x in range(0, self.numberOfColumns) and y in range(0, self.numberOfRows):
			self.board.open(x, y)
			self.update()

			if self.board.nodes[x][y].type == -1:
				print("Game over, you deaded!")
				self.game = False

	def markCell( self, event ):
		if not self.game:
			return

		x = floor((event.x - 2 - self.boardAdjustmentX) / self.cellWidth)
		y = floor((event.y - 3 - self.boardAdjustmentY) / self.cellHeight)

		if x in range(0, self.numberOfColumns) and y in range(0, self.numberOfRows):
			self.board.mark(x, y)
			self.update()

	def update(self):
		for x in range (self.numberOfColumns):
			for y in range(self.numberOfRows):
				if not self.board.nodes[x][y].open:
					self.canvas.create_rectangle(self.boardAdjustmentX + x * self.cellWidth, self.boardAdjustmentY + y * self.cellHeight, self.boardAdjustmentX + (x + 1) * self.cellWidth, self.boardAdjustmentY + (y + 1) * self.cellHeight, fill = "#696969")
				elif self.board.nodes[x][y].type == -1:
					self.canvas.create_rectangle(self.boardAdjustmentX + x * self.cellWidth, self.boardAdjustmentY + y * self.cellHeight, self.boardAdjustmentX + (x + 1) * self.cellWidth, self.boardAdjustmentY + (y + 1) * self.cellHeight, fill = "#FF0000")
				else:
					self.canvas.create_rectangle(self.boardAdjustmentX + x * self.cellWidth, self.boardAdjustmentY + y * self.cellHeight, self.boardAdjustmentX + (x + 1) * self.cellWidth, self.boardAdjustmentY + (y + 1) * self.cellHeight, fill = "#FFE4B5")

		for x in range (self.numberOfColumns):
			for y in range(self.numberOfRows):
				if self.board.nodes[x][y].open:
					if self.board.nodes[x][y].type != 0:
						self.canvas.create_text(self.boardAdjustmentX + x * self.cellWidth + 10, self.boardAdjustmentY + y * self.cellHeight + 10, text = str(self.board.nodes[x][y].type))
				elif self.board.nodes[x][y].mark:
					self.canvas.create_rectangle(self.boardAdjustmentX + x * self.cellWidth + self.cellWidth / 2 - 2, 
													self.boardAdjustmentY + y * self.cellHeight + self.cellHeight / 2 - 2, 
													self.boardAdjustmentX + x * self.cellWidth + self.cellWidth / 2 + 2, 
													self.boardAdjustmentY + y * self.cellHeight + self.cellHeight / 2 + 2, fill = "#FF0000")

		if self.board.checkBoard():
			print ("You won!")
			self.game = False

def main():
	root = Tk()
	assHole = Minefield(root)
	root.mainloop()

# I have no idea what I'm doing :D
if __name__ == "__main__":
	main()