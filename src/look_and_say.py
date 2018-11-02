import itertools

def look_and_say(n):
	def next_number(nums):
		curr = nums[-1]
		groups = itertools.groupby(curr)
		nums.append(''.join([str(len(list(group))) + key for key, group in groups]))

	nums = ['1']
	for _ in range(1, n):
		next_number(nums)
	return nums

print(look_and_say(8))