'''
class node(object):
	def __init__(self, value, children=[]):
		self.value = value
		self.children = children



class BinaryTree():
	def __init__(self, rootid):
		self.left = None
		self.right = None
		self.rootid = rootid

	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def setNodeValue(self, value):
		self.rootid = value
	def getNodeValue(self):
		return self.rootid

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			tree = BinaryTree(newNode)
			tree.right = tree
			self.right = tree

	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			self.left = tree
			tree.left = self.left

def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())


myTree = None
'''

lines = []
with open('problem18.txt') as f:
	for line in f:
		if not line:
			break
		else:
			line = line.replace('\n', '')
			lines.append(line)


def getLine(i):
	after = []
	current = lines[len(lines) - i]
	for s in current.split(' '):
		n = int(s)
		after.append(n)
	return after


def getNewLine(numBottom, numSecondBottom):
	nums = []

	for i in range(0, len(numSecondBottom)):
		n = numSecondBottom[i]
		left = numBottom[i] + numSecondBottom[i]
		right = numBottom[i+1] + numSecondBottom[i]
		if left > right:
			nums.append(left)
		else:
			nums.append(right)

	return nums


line1 = []

for i in range(1, len(lines)):
	if i == 1:
		line1 = getLine(i)
	
	line2 = getLine(i+1)
	line1 = getNewLine(line1, line2)

	print line1
	print line2