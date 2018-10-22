def even_odd(nums):
	left = 0
	right = len(nums) - 1
	while left < right:
		if nums[left] & 1: # is even
			nums[left], nums[right] = nums[right], nums[left]
			right -= 1
		else: # number is odd
			left += 1
	return nums

nums = [1,2,3,4,5,6,7,8]
print(even_odd(nums))


def tripartition(nums, pivot):
	pivot = nums[pivot]
	right = len(nums) - 1
	next_pivot = 0
	pos = 0
	while pos <= right:
		if nums[pos] == pivot:
			if pos == next_pivot:
				pos += 1
				next_pivot += 1
			else:
				nums[next_pivot], nums[pos] = nums[pos], nums[next_pivot]
				next_pivot += 1
		elif nums[pos] > pivot:
			nums[right], nums[pos] = nums[pos], nums[right]
			right -= 1
		else:
			pos += 1
	return nums[next_pivot:pos], nums[:next_pivot], nums[pos:]

nums = [6, 5, 2, 7, 3, 2, 8, 5, 22, 3, 4, 7, 8, 0, 45,8 ]
pivot = nums.index(8)
print(tripartition(nums, pivot))

def tri_inplace(nums, pivot, left=None, right=None):
	pivot = nums[pivot]
	left = 0 if left is None else left
	right = len(nums) - 1 if right is None else right
	# first move all numbers greater than pivot to the right side of array
	next_right = right
	next_left = left
	while next_left <= next_right:
		if nums[next_left] > pivot:
			nums[next_left], nums[next_right] = nums[next_right], nums[next_left]
			next_right -= 1
		else:
			next_left += 1
	# next move all numbers equal to pivot to the middle of array right
	mid = next_right
	next_left = left
	while next_left <= mid: # less than or equal to because we need to ensure the number at mid is processed
		if nums[next_left] == pivot:
			nums[next_left], nums[mid] = nums[mid], nums[next_left]
			mid -= 1
		else:
			next_left += 1
	# mid + 1 is the starting index of pivots
	# right + 1 is the starting index of numbers greater than pivot
	return (mid + 1, next_right + 1)

def quicksort(nums):
	if not nums:
		return []
	if len(nums) == 1:
		return nums
	if len(nums) == 2:
		return [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]
	pivot = len(nums) // 2
	left, pivots, right = tripartition(nums, pivot)
	return quicksort(left) + pivots + quicksort(right)

def quicksort_inplace(nums, left=None, right=None):
	if not nums:
		return
	if len(nums) == 1:
		return
	left = 0 if left is None else left
	right = len(nums) - 1 if right is None else right
	if left >= right:
		return
	pivot = (right + left) // 2
	left_end, right_start = tri_inplace(nums, pivot, left, right)
	quicksort_inplace(nums, left, left_end)
	quicksort_inplace(nums, right_start, right)

nums = [1, 2, -1, 4, -4, 2, 0, 6, -12]
sorted_nums = nums[:]
quicksort_inplace(sorted_nums)
assert sorted_nums == sorted(nums)