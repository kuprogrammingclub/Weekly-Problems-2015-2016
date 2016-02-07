class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value < self.value:
			if self.left == None:
				self.left = Node(value)
			else:
				self.left.insert(value)
		else:
			if self.right == None:
				self.right = Node(value)
			else:
				self.right.insert(value)

	def height(self):
		leftheight = self.left.height() if self.left != None else 0
		rightheight = self.right.height() if self.right != None else 0
		return max([leftheight, rightheight]) + 1

