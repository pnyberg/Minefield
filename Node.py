class Node:
	def __init__(self):
		self.type = 0
		self.open = False
		self.mark = False

	def setType(self, type):
		self.type = type

	def openNode(self):
		if self.open:
			return False
		self.open = True
		return self.type == 0

	def fixMark(self):
		self.mark = not self.mark