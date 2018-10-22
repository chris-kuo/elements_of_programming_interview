import unittest
import random

import arrays

def less_than(b, arr):
	return all([a < b for a in arr])

def greater_than(b, arr):
	return all([a > b for a in arr])

class DutchFlagPartitionTest(unittest.TestCase):
	def setUp(self):
		self.rand_ints = [random.randint(-100, 100) for _ in range(20)]
		self.reverse_ints = list(reversed(range(-20, 20, 3)))

	def test_null_input(self):
		self.assertEqual([], arrays.dutch_flag_partition(3, []))

	def test_random_input(self):
		B = list(self.rand_ints)
		pivot_index = len(B) // 2
		pivot = B[pivot_index]
		arrays.dutch_flag_partition(pivot_index, B)
		self.assertTrue(less_than(pivot, B[:B.index(pivot)]))
		self.assertTrue(greater_than(pivot, B[B.index(pivot) + B.count(pivot):]))

	def test_reverse_input(self):
		B = list(self.rand_ints)
		pivot_index = len(B) // 2
		pivot = B[pivot_index]
		arrays.dutch_flag_partition(pivot_index, B)
		self.assertTrue(less_than(pivot, B[:B.index(pivot)]))
		self.assertTrue(greater_than(pivot, B[B.index(pivot) + B.count(pivot):]))

class PartitionTristateTest(unittest.TestCase):
	def check_partition(self, states, arr):
		a, b, c = states
		a_index = arr.index(a) if a in arr else -1
		b_index = arr.index(b) if b in arr else a_index
		c_index = arr.index(c) if c in arr else max(a_index, b_index)
		self.assertTrue(a_index <= b_index)
		self.assertTrue(b_index <= c_index)

	def test_random_int_input(self):
		states = [random.randint(-10, 10) for _ in range(3)]
		arr = random.choices(states, k=100) + states
		a, b, c = states
		arrays.partition_tristate(arr, states)
		self.check_partition(states, arr)

	def test_random_str_input(self):
		chars = 'abcdefghijklmnopqrstuvwxyz'
		states = []
		while len(set(states)) < 3:
			a = ''.join(random.choices(chars, k=random.randint(1, 10)))
			b = ''.join(random.choices(chars, k=random.randint(1, 10)))
			c = ''.join(random.choices(chars, k=random.randint(1, 10)))
			states = (a, b, c)
		arr = random.choices(states, k=random.randint(1, 50))
		arrays.partition_tristate(arr, states)
		self.check_partition(states, arr)
	
	
	def test_incremental_length_input(self):
		chars = 'abcdefghijklmnopqrstuvwxyz'
		for N in range(100):
			for _ in range(100): # repeat each length 100 times
				states = []
				while len(set(states)) != 3:
					a = ''.join(random.choices(chars, k=random.randint(1, 10)))
					b = ''.join(random.choices(chars, k=random.randint(1, 10)))
					c = ''.join(random.choices(chars, k=random.randint(1, 10)))
					states = (a, b, c)
				arr = random.choices(states, k=N)
				arrays.partition_tristate(arr, states)
				self.check_partition(states, arr)
		


class PartitionQuadstateTest(unittest.TestCase):
	def check_partition(self, states, arr):
		a, b, c, d = states
		a_index = arr.index(a) if a in arr else -1
		b_index = arr.index(b) if b in arr else a_index
		c_index = arr.index(c) if c in arr else b_index
		d_index = arr.index(d) if d in arr else c_index
		self.assertTrue(a_index <= b_index)
		self.assertTrue(b_index <= c_index)
		self.assertTrue(c_index <= d_index)

	def test_valid_input(self):
		states = ['a', 'b', 'c', 'd']
		arr = random.choices(states, k=20)
		arrays.partition_quadstate(arr, states)
		self.check_partition(states, arr)

class PlusOneTest(unittest.TestCase):
	def test_valid_input(self):
		self.assertEqual(arrays.plus_one(list('129')), list('130'))
		self.assertEqual(arrays.plus_one(list('123')), list('124'))
		self.assertEqual(arrays.plus_one(list('9921')), list('9922'))
		self.assertEqual(arrays.plus_one(list('9999')), list('10000'))

class CanReachEndTest(unittest.TestCase):
	def test_reachable(self):
		self.assertTrue(arrays.can_reach_end([3,3,1,0,2,0,1]))
		self.assertTrue(arrays.can_reach_end([3,2,0,0,2,0,1]))

class DeleteDuplicatesTest(unittest.TestCase):
	def test_valid_inputs(self):
		self.assertEqual(arrays.delete_duplicates([2,3,5,5,7,11,11,11,13]), [2,3,5,7, 11, 13])
		self.assertEqual(arrays.delete_duplicates([]), [])

if __name__ == '__main__':
	unittest.main()