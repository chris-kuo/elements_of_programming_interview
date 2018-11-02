from collections import deque

class BinaryTree():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def binary_tree_depth_order(tree):
	'''
	Return elements in binary tree grouped in depth order of increasing depth
	'''
	result = []
	if not tree:
		return result
	current_depth_nodes = [tree]
	while current_depth_nodes:
		# add all current nodes to result
		result.append([curr.data for curr in current_depth_nodes])
		# add children nodes to nodes list
		current_depth_nodes = [child for curr in current_depth_nodes
				for child in (curr.left, curr.right) if child]
	return result

tree11 = BinaryTree(11)
tree10 = BinaryTree(10)
tree9 = BinaryTree(9)
tree8 = BinaryTree(8)
tree4 = BinaryTree(4)
tree5 = BinaryTree(5, tree8)
tree6 = BinaryTree(6, None, tree9)
tree7 = BinaryTree(7, tree10, tree11)
tree2 = BinaryTree(2, tree4, tree5)
tree3 = BinaryTree(3, tree6, tree7)
tree = BinaryTree(1, tree2, tree3)

print(binary_tree_depth_order(tree))

def binary_tree_alternating_depth_order(tree):
	'''
	Return elements in binary tree grouped in depth order of increasing depth
	'''
	result = []
	if not tree:
		return result
	current_depth_nodes = [tree]
	left_right = True
	while current_depth_nodes:
		# add all current nodes to result
		result.append([curr.data for curr in 
				(current_depth_nodes if left_right else
				reversed(current_depth_nodes))])
		# add children nodes to nodes list
		current_depth_nodes = [child for curr in current_depth_nodes
				for child in (curr.left, curr.right) if child]
		left_right = not left_right
	return result
print(binary_tree_alternating_depth_order(tree))

def binary_tree_reverse_depth_order(tree):
	'''
	Return elements of binary tree in bottom-up left-right order
	'''
	result = []
	if not tree:
		return result
	current_depth_nodes = [tree]
	while current_depth_nodes:
		result.append([curr.data for curr in current_depth_nodes])
		current_depth_nodes = [
			child for curr in current_depth_nodes
			for child in (curr.left, curr.right)
			if child
		]
	return result[::-1]

print(binary_tree_reverse_depth_order(tree))

def binary_tree_average_for_depth(tree):
	'''
	Return the average key for all keys in the same depth for 
	each depth
	'''
	result = []
	if not tree:
		return result
	current_depth_nodes = [tree]
	while current_depth_nodes:
		result.append(
			sum([curr.data for curr in current_depth_nodes])
			/ len(current_depth_nodes)
		)
		current_depth_nodes = [
			child for curr in current_depth_nodes
			for child in (curr.left, curr.right) if child]
	return result

print(binary_tree_average_for_depth(tree))

class QueueWithMax():
	def __init__(self):
		self.queue = deque()
		self.max_queue = deque()

	def enque(self, item):
		self.queue.append(item)
		while  self.max_queue and self.max_queue[-1] < item:
			self.max_queue.pop()
		self.max_queue.append(item)

	def deque(self):
		if not self.queue:
			raise IndexError('Cannot deque from empty queue')
		item = self.queue.popleft()
		if item == self.max_queue[0]:
			self.max_queue.popleft()
		return item

	def max(self):
		if not self.max_queue:
			raise IndexError('Cannot get max from empty queue')
		return self.max_queue[0]

	def __str__(self):
		return str(self.queue)

queue = QueueWithMax()
queue.enque(1)
queue.enque(2)
queue.enque(8)
queue.enque(4)
queue.enque(5)
print(queue, queue.max())
print('deque:', queue.deque(), '--', queue, queue.max())
print('deque:', queue.deque(), '--', queue, queue.max())
print('deque:', queue.deque(), '--', queue, queue.max())
print('deque:', queue.deque(), '--', queue, queue.max())
queue.enque(5)
queue.enque(4)
queue.enque(3)
queue.enque(4)
queue.enque(1)
print('deque:', queue.deque(), '--', queue, queue.max())
print('deque:', queue.deque(), '--', queue, queue.max())
print('deque:', queue.deque(), '--', queue, queue.max())
print('deque:', queue.deque(), '--', queue, queue.max())
print('deque:', queue.deque(), '--', queue, queue.max())