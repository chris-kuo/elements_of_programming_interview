import random
import collections


class Stack_with_cached_max():
	def __init__(self):
		self.stack = []
		self.cached_max = []
		self.cached_max_count = []

	def __str__(self):
		return str(self.stack)

	def is_empty(self):
		return len(self.stack) == 0

	def push(self, val):
		if self.is_empty():
			self.cached_max.append(val)
			self.cached_max_count.append(1)
		else:
			if val > self.cached_max[-1]:
				self.cached_max.append(val)
				self.cached_max_count.append(1)
			elif val == self.cached_max[-1]:
				self.cached_max_count[-1] += 1	
		self.stack.append(val)

	def pop(self):
		if len(self.stack) == 0:
			return None
		if self.stack[-1] == self.cached_max[-1]:
			# popping off a max value
			self.cached_max_count[-1] -= 1
			if self.cached_max_count[-1] == 0: # exhausted current max
				self.cached_max.pop()
				self.cached_max_count.pop()
		return self.stack.pop()

	def max(self):
		return self.cached_max[-1] if self.cached_max else None



stack = Stack_with_cached_max()
print(stack, 'max =', stack.max())
stack.push(1)
stack.push(2)
stack.push(1)
print(stack, 'max =', stack.max())
stack.push(2)
stack.push(6)
stack.push(6)
stack.push(4)
stack.push(5)
print(stack, 'max =', stack.max())
print('popped', stack.pop())
print(stack, 'max =', stack.max())
print('popped', stack.pop())
for _ in range(8):
	print('popped', stack.pop(), 'stack:', stack, 'max:', stack.max())
stack.push(1)
stack.push(2)
stack.push(1)
print(stack, 'max =', stack.max())
stack.push(2)
stack.push(6)
print(stack, 'max =', stack.max())


def eval_rpn(rpn_exp):
	'''
	Evaluate RPN expression. Supported operations are +, -, *, /
	'''
	stack = [] # stores integer expressions
	tokens = rpn_exp.split()
	acc = 0 # accumulator
	for t in tokens:
		if t in '+-*/':
			op2 = stack.pop()
			op1 = stack.pop()
			if t == '+':
				stack.append(op1 + op2)
			elif t == '-':
				stack.append(op1 - op2)
			elif t == '*':
				stack.append(op1 * op2)
			elif t == '/':
				stack.append(op1 / op2)
		else: # assumes t is a number
			stack.append(float(t))
	return stack

s = '1 4 +'
print(s, eval_rpn(s))
s = '1 4 + 6'
print(s, eval_rpn(s))
s = '3 4 + 2 * 1 +'
print(s, eval_rpn(s))


def is_well_formed(s):
	'''
	A string is well formed if all of it's left parenthesis (, [, { are
	matched with correct right parenthesis
	'''
	left_parens = []
	match = {')': '(', 
			']': '[', 
			'}': '{'}
	for c in s:
		if c in '([{':
			left_parens.append(c)
		elif c in ')]}':
			if left_parens.pop() != match[c]:
				return False
	# should have no left parenthesis left
	return len(left_parens) == 0

assert is_well_formed('()[]{}') == True
assert is_well_formed('([)]') == False
assert is_well_formed('([({   })  afa evc ] -- )') == True
assert is_well_formed('( [ ( { [ ] () }') == False

def shortest_equivalent_path(path):
	# cases:
	# empty string
	# relative path (doens't start with /)
	# absolute path (starts with /)
	if not path:
		raise ValueError('Empty string is not valid path')
	path_names = [] # use as stack for current path
	if path[0] == '/':
		path_names.append('/')
	for token in (token for token in path.split('/') if token not in ['/', '']):
		if token == '..':
			# if it's relative path
			if not path_names or path_names[-1] == '..':
				path_names.append('..')
			else:
				if path_names[-1] == '/':
					raise ValueError('Path error')
				path_names.pop()
		else: # must be name
			path_names.append(token)
	result = '/'.join(path_names)
	return result[result.startswith('//'):]

def buildings_with_sunset_view(sequence):
	'''
	building height given in east-to-west sequence
	buildings have window on west, and has sunset view
	if all buildings to the west are shorter
	'''
	candidates = []
	Building = collections.namedtuple('Building', ('id', 'height'))

	for i, h in enumerate(sequence):
		if len(candidates) == 0:
			candidates.append(Building(id=i, height=h))
		else:
			# pop all buildings shorter or equail to s
			while candidates[-1].height <= h:
				candidates.pop()
			candidates.append(Building(i, h))
	return candidates

buildings = [9, 5, 7, 4, 4, 2, 6, 1, 1]
print(buildings)
print(buildings_with_sunset_view(buildings))
