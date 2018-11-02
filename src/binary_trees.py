from collections import deque, namedtuple, defaultdict

class BinaryTreeNode():
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def inorder(tree, fn):
	if tree:
		inorder(tree.left, fn)
		fn(tree.data)
		inorder(tree.right, fn)

def preorder(tree, fn, ret=None, default=None):
	if tree:
		ret = fn(tree.data, ret)
		if not ret:
			ret = default
		preorder(tree.left, fn, ret)
		preorder(tree.right, fn, ret)

def postorder(tree, fn, lret=None, rret=None, default=None):
	if tree:
		lret = postorder(tree.left, fn, default=default)
		if not lret:
			lret = default
		rret = postorder(tree.right, fn, default=default)
		if not rret:
			rret = default
		return fn(tree.data, lret, rret)


D = BinaryTreeNode(28)
E = BinaryTreeNode(0)
C = BinaryTreeNode(271, D, E)

H = BinaryTreeNode(17)
G = BinaryTreeNode(3, H, None)
F = BinaryTreeNode(561, None, G)

B = BinaryTreeNode(6, C, F)

Q = BinaryTreeNode(142)
M = BinaryTreeNode(641)
L = BinaryTreeNode(401, Q, M)
N = BinaryTreeNode(257)
K = BinaryTreeNode(1, L, N)
J = BinaryTreeNode(2, None, K)

P = BinaryTreeNode(28)
O = BinaryTreeNode(271, None, P)
I = BinaryTreeNode(6, J, O)

A = BinaryTreeNode(314, B, I)

print(postorder(A, lambda d, left, right: d + left + right, default=0))
postorder(A, print)

def is_balanced_tree(tree):
	'''
	Return True if tree is balanced, False if not
	A tree is balanced if the height of its left tree and its right tree
	differ by equal or less than 1
	'''
	
	BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ['balanced', 'height'])
	
	def check_balance(tree):
		'''Chech if tree is balanced. Returns BalancedStatusWithHeight'''
		# base case
		if not tree:
			return BalancedStatusWithHeight(True, -1)
		# recursive cases
		# check left tree
		left_result = check_balance(tree.left)
		if not left_result.balanced:
			return BalancedStatusWithHeight(False, -1)
		# check right tree
		right_result = check_balance(tree.right)
		if not right_result.balanced:
			return BalancedStatusWithHeight(False, -1)
		# assert: both left and right trees are balanced
		is_balanced = abs(left_result.height - right_result.height) <= 1
		height = 1 + max(left_result.height, right_result.height)
		return BalancedStatusWithHeight(is_balanced, height)

	return check_balance(tree).balanced

def largest_complete_subtree(tree):
	'''
	Returns the size (width) of the largest complete subtree
	'''


print('----- Balanced Tree Tests -----')
print(is_balanced_tree(A))
print(is_balanced_tree(B))
print(is_balanced_tree(C))

def largest_complete_subtree(tree):
	'''
	Return the number of nodes of the largest complete 
	tree in tree
	'''
	StatusWithHeight = namedtuple('StatusWithHeight', ['complete', 'lh', 'rh', 'size'])

	def check_subtree(tree):
		# base case
		if not tree:
			return StatusWithHeight(True, 0, 0, 0)
		left_result = check_subtree(tree.left)
		right_result = check_subtree(tree.right)
		# for a tree to be complete, the total height difference
		# between left and right cannot exceed 1, and the 
		# heights have to be in equal or descreasing order
		size = max(left_result.size, right_result.size)
		if not left_result.complete or not right_result.complete:
			return StatusWithHeight(False, -1, -1, size)
		heights = [left_result.lh, left_result.rh, right_result.lh, right_result.rh]
		if heights != sorted(heights, reverse=True):
			return StatusWithHeight(False, -1, -1, size)
		# assert: the heights are in ascending order
		# check difference between heights don't exceed by 1
		if left_result.lh - right_result.rh > 1:
			return StatusWithHeight(False, -1, -1, size)
		# assert: tree is a complete tree
		return StatusWithHeight(True, left_result.lh + 1, right_result.rh + 1, left_result.size + right_result.size + 1)

	return check_subtree(tree).size

print('----- Starting largest complete subtree test -----')
print(largest_complete_subtree(A), '?= 5')


def is_symmetric(tree):
	# a tree is symmetric if its left and right subtree are reflections
	# of each other
	def check_subtree(left, right):
		# base case
		if not left and not right:
			return True
		# assert: at least one of left or right is not None
		elif left and right:
			return left.data == right.data and \
				check_subtree(left.left, right.right) and check_subtree(left.right, right.left)
		return False
	return not tree or check_subtree(tree.left, tree.right)

d = BinaryTreeNode(3)
c = BinaryTreeNode(2, None, d)
b = BinaryTreeNode(6, None, c)
g = BinaryTreeNode(3)
f = BinaryTreeNode(2, g)
e = BinaryTreeNode(6, f)
a = BinaryTreeNode(314, b, e)

print('----- Starting symmetric binary tree test -----')
print(is_symmetric(a), '?= True')
e.data = 5
print(is_symmetric(a), '?= False')
e.data = 6
f.left = None
print(is_symmetric(a), '?= False')
print(is_symmetric(None))

def sum_root_to_leaf(tree, partial_path_sum=0):
	# null input
	if not tree:
		return 0
	# Calculate partial path sum
	partial_path_sum = partial_path_sum * 2 + tree.data
	# leaf node
	if not tree.left and not tree.right:
		print(bin(partial_path_sum))
		return partial_path_sum
	# non-leaf node
	left_sum = sum_root_to_leaf(tree.left, partial_path_sum)
	right_sum = sum_root_to_leaf(tree.right, partial_path_sum)
	return left_sum + right_sum

d = BinaryTreeNode(0)
e = BinaryTreeNode(1)
c = BinaryTreeNode(0, d, e)
h = BinaryTreeNode(0)
g = BinaryTreeNode(1, h)
f = BinaryTreeNode(1, None, g)
b = BinaryTreeNode(0, c, f)
m = BinaryTreeNode(1)
l = BinaryTreeNode(1, None, m)
n = BinaryTreeNode(0)
k = BinaryTreeNode(0, l, n)
j = BinaryTreeNode(0, None, k)
p = BinaryTreeNode(0)
o = BinaryTreeNode(0, None, p)
i = BinaryTreeNode(1, j, o)
a = BinaryTreeNode(1, b, i)

print('----- Starting sum root to leaf tests -----')
print(bin(sum_root_to_leaf(a)))


def has_path_sum(tree, remaining_weight):
	# null input
	if not tree:
		return True if remaining_weight == 0 else False
	remaining_weight -= remaining_weight
	# leaf node
	if not tree.left and not tree.right:
		return True if remaining_weight == 0 else False
	# non-leaf node
	return has_path_sum(tree.left, remaining_weight) or \
			has_path_sum(tree.right, remaining_weight)

print('----- Starting has path sum test ------')
print(has_path_sum(A, 50), '?= False')
print(has_path_sum(A, 580), '?= True')


def path_sum_equals(tree, remaining_weight):
	# null input
	result = []
	if not tree:
		return result
	# leaf node
	if not tree.left and not tree.right:
		if remaining_weight == tree.data:
			result.append([tree.data])
		# non-leaf node
	else:
		remaining_weight -= tree.data
		result += path_sum_equals(tree.left, remaining_weight)
		result += path_sum_equals(tree.right, remaining_weight)
		result = [[tree.data] + partial_path for partial_path in result]
	return result

print('----- Starting path_sum_equals test -----')
print(path_sum_equals(A, 619))


def inorder_trasversal(tree, fn=print):
	'''non-recursion implementation of in order transversal of tree'''
	# use a stack to backtrack, backtrack when hit None node
	stack = []
	while stack or tree:
		if tree:
			# go left
			stack.append(tree)
			tree = tree.left
		else:
			# go back up
			tree = stack.pop()
			fn(tree.data)
			# go right
			tree = tree.right

print('----- Starting in order transversal without recursion test -----')
inorder_trasversal(A, print)


def preorder_trasversal(tree, fn=print):
	''' non-recursive implementation of pre order transversal of tree'''
	# use stack to backtrack
	stack = []
	while tree or stack:
		if tree:
			fn(tree.data) # process node
			# add right node to queue and go left
			stack.append(tree.right)
			tree = tree.left
		else:
			# backtrack
			tree = stack.pop()

print('----- Starting pre order transversal without recursion test -----')
preorder_trasversal(A, print)

def postorder_traversal(tree, fn=print):
	'''non-recursive implementation of post order tranversal of tree'''
	stack = []
	while tree or stack:
		if tree:
			if tree.right:
				stack.append(tree.right)
			stack.append(tree)
			# go left
			tree = tree.left
		else:
			# check if last item in stack has right child in stack
			tree = stack.pop()
			if stack and stack[-1] is tree.right:
				# swap
				stack[-1], tree = tree, stack[-1]
			else:
				# process node
				fn(tree.data)
				tree = None
print('----- Starting post order transversal without recursion test -----')
postorder_traversal(A, print)