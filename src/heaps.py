import heapq
import itertools
import math

def sort_approximately_sorted_array(sequence, k):
	result = []
	min_heap = []

	for x in itertools.islice(sequence, k):
		heapq.heappush(min_heap, x)

	for x in sequence:
		smallest = heapq.heappushpop(min_heap, x)
		result.append(smallest)

	while min_heap:
		result.append(heapq.heappop(min_heap))

	return result

print(sort_approximately_sorted_array([1,2,3,6,5,7,8,10,8, 9, 11, 12], 3))

class Star:
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z

	@property
	def distance(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def __lt__(self, rhs):
		return self.distance < rhs.distance

	def __str__(self):
		return 'Star(%s, %s, %s)' % tuple(map(str, (self.x, self.y, self.z)))

def find_closest_k_stars(stars, k):
	# use max heap to store the closes k stars
	max_heap = []
	for star in stars:
		heapq.heappush(max_heap, (-star.distance, star))
		if len(max_heap) > k:
			heapq.heappop(max_heap)
	return [s[1] for s in heapq.nlargest(k, max_heap)]

stars = [Star(x, y, z) for x, y, z in [(1,2,3), (4,5,6), (0,1,1), (-1,-1,0), (4,3,2), (1, 2, 0), (-2, 0, 1),(3,  7, -1)]]
print([str(star) for star in find_closest_k_stars(stars, 3)])


def online_median(sequence):
	# splits sequence into 2 halves, one greater than median
	# the other less
	min_heap = [] # upper half
	max_heap = [] # lower half
	result = []

	for x in sequence:
		heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
		if len(max_heap) > len(min_heap): # ensure both heap have same length, or min_heap has 1 more
			heapq.heappush(min_heap, -heapq.heappop(max_heap))
		result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0])
	return result

print(online_median([1,2,3,4,5,6,7,8,9,0]))	
