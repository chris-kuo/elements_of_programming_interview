def dutch_flag_partition(pivot_index, arr):
	# [0:bottom] contains element smaller than pivot
	# [bottom:mid] contains element equal to pivot
	# [mid:top] contains unclassified elements
	# [top:<end>] contains elements greater than pivot
	if not arr:
		return []
	if pivot_index < 0 or pivot_index >= len(arr):
		raise IndexError()

	pivot = arr[pivot_index]
	bottom = 0
	mid = 0
	top = len(arr) 

	while mid < top:
		if arr[mid] == pivot:
			mid += 1
		elif arr[mid] < pivot:
			arr[bottom], arr[mid] = arr[mid], arr[bottom]
			bottom += 1
			mid += 1 # the element from arr[bottom] is already classified
		elif arr[mid] > pivot:
			top -= 1  # need to decrement index first, since top points to current first of elements greater than pivot
			arr[top], arr[mid] = arr[mid], arr[top]

def partition_tristate(arr, states):
	# assumes arr can take on 3 states given in <states>
	second = 0
	unclassified = 0
	third = len(arr)
	a, b, c = states
	while unclassified < third:
		if arr[unclassified] == a: # first state
			arr[second], arr[unclassified] = arr[unclassified], arr[second]
			unclassified += 1
			second += 1
		elif arr[unclassified] == b: # second state
			unclassified += 1
		elif arr[unclassified] == c: # third statem
			third -= 1
			arr[third], arr[unclassified] = arr[unclassified], arr[third]

def partition_quadstate(arr, states):
	"""
	arr[:i] contains first states, i.e. state a
	arr[i:unknown] contains second states, ie state b
	arr[unknonw, j] contains unclassified states
	arr[j:k] contains thrid states, ie state c
	arr[k:] contains fourth states, ie state d

	[0, i], [i, unknown], <unknown, j>, [j, k], [k:end]
	"""
	a, b, c, d = states
	i, unknown, j, k  = 0, 0, len(arr), len(arr)

	while unknown < j:
		val = arr[unknown]
		if val == a:
			arr[i], arr[unknown] = arr[unknown], arr[i]
			i += 1
			unknown += 1
		elif val == b:
			unknown += 1
		elif val == c:
			j -= 1
			arr[j], arr[unknown] = arr[unknown], arr[j]
		elif val == d:
			k -= 1
			j -= 1
			arr[unknown], arr[j], arr[k] = arr[j], arr[k], arr[unknown]

def plus_one(A):
	# assume inputs are valid
	# A is an array of char of digits
	digits = '0123456789'
	digit_incr = '1234567890'
	carry = True
	for i in reversed(range(len(A))):
		d = A[i]
		if carry:
			carry = True if d == '9' else False
			A[i] = digit_incr[digits.index(d)]
	# check if there is carry
	if carry:
		# insert digit to the left
		A.insert(0, '1')
	return A

def can_reach_end(arr):
	furtherest_reachable = 0
	pos = 0
	N = len(arr)
	while pos <= furtherest_reachable and furtherest_reachable < N - 1:
		furtherest_reachable += arr[pos]
		pos += 1
	return True if furtherest_reachable >= N - 1 else False

def delete_duplicates(arr):
	if not arr:
		return arr
	assert arr == sorted(arr)
	last_unique = arr[0]
	next_pos = 1
	num_to_delete = 0
	for i in range(1, len(arr)):
		if arr[i] == last_unique:
			# delete this entry
			num_to_delete += 1
		else: # found another unique number
			last_unique = arr[i]
			arr[next_pos] = last_unique
			next_pos += 1
	if num_to_delete > 0:
		del arr[-num_to_delete:]
	return arr

def delete_from_array(arr, items):
	if not arr:
		return arr
	next_pos = 0
	num_remaining = len(arr)
	for i in range(len(arr)):
		if arr[i] in items:
			# remove entry
			num_remaining -= 1
		else: # keep entry. Copy to next position
			arr[next_pos] = arr[i]
			next_pos += 1
	# delete entries
	del arr[num_remaining:]
	return arr

def m_times_to_twice(arr, m):
	'''
	if an item appears exactly m times in sorted array arr, it is
	updated to appear exactly twice
	'''
	if not arr:
		return arr
	occurrences = 0
	next_pos = 0
	val = arr[0]
	for i in range(len(arr)):
		if arr[i] == val:
			occurrences += 1
		else: # val != arr[i]
			# check occurrences
			if occurrences == m:
				arr[next_pos], arr[next_pos+1] = val, val
				next_pos += 2
				val = arr[i]
				occurrences = 1
			else:
				arr[next_pos:next_pos+occurrences] = [val] * occurrences
				next_pos += occurrences
				val = arr[i]
				occurrences = 1
	# fill in occurrences of last unique number
	arr[next_pos:next_pos+occurrences] = [val] * occurrences
	del arr[next_pos + occurrences:]
	return arr

def buy_sell_stock_once(prices):
	# The profit of buying at i-th day is proportional to the maximum
	# stock price that comes after
	# max profit

	# first determine the maximum price at or after position i
	N = len(prices)
	max_after = [prices[-1]] * N
	for i in reversed(range(N-1)):
		max_after[i] = prices[i] if prices[i] > max_after[i+1] else max_after[i+1]
	profits = [max_after[i] - prices[i] for i in range(N)]
	return max(profits)

def buy_sell_stock_twice(prices):
	# TODO: solve this problem in O(n) time and O(1) space
	N = len(prices)
	lowest_price_so_far = float('Inf')
	maximum_profit = 0.0
	profit_by_i = [0] * N
	for i, price in enumerate(prices):
		lowest_price_so_far = min(lowest_price_so_far, price)
		maximum_profit = max(maximum_profit, price - lowest_price_so_far)
		profit_by_i[i] = maximum_profit
	highest_price_so_far = float('-Inf')
	maximum_profit = 0.0
	for i, price in reversed(list(enumerate(prices[1:], 1))):
		highest_price_so_far = max(highest_price_so_far, price)
		maximum_profit = max(maximum_profit, highest_price_so_far - price + profit_by_i[i-1])
	return maximum_profit

def rearrange(A):
	'''
	Rearrange elements in A so that A[0] <= A[1] >= A[2] ...
	'''
	A.sort()
	for i in range(1, len(A) - 1, 2):
		A[i], A[i+1] = A[i+1], A[i]
	return A