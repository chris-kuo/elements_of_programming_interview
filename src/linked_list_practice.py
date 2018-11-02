from LinkedList import ListNode
import random

def merge(L1, L2):
	dummy = ListNode()
	tail = dummy # hold the last node in merged list
	while L1 and L2:
		if L1.data < L2.data:
			tail.next = L1
			L1 = L1.next
		else:
			tail.next = L2
			L2 = L2.next
		tail = tail.next
	# either L1 or L2 is empty
	if L1:
		tail.next = L1
	if L2:
		tail.next = L2
	return dummy.next

a4 = ListNode(9)
a3 = ListNode(4, a4)
a2 = ListNode(3, a3)
a1 = ListNode(-3, a2)
a = ListNode(-10, a1)

b3 = ListNode(10)
b2 = ListNode(5, b3)
b1 = ListNode(-2, b2)
b = ListNode(-10, b1)

def print_linked_list(L):
	while L:
		print(L.data, end=', ')
		L = L.next
	print()

print_linked_list(a)
print_linked_list(b)
c = merge(a, b)
print_linked_list(c)

def reverse_list(L):
	# reverse linked list L
	if not L:
		return L
	new_head = L
	L = L.next
	new_head.next = None # detach
	while L:
		next = L.next
		L.next = new_head
		new_head = L
		L = next
	return new_head

c = reverse_list(c)
print_linked_list(c)


def reverse_sublist(L, start, finish):
	# reverse start-th to finish-th nodes within linked list L,
	# inclusive.
	sublist_parent = dummy = ListNode()
	dummy.next = L
	for _ in range(1, start):
		sublist_parent = sublist_parent.next
	sublist_tail = sublist_parent.next
	for _ in range(finish - start):
		# only need to swap iter with next if at least 2 nodes are
		# being swapped
		temp = sublist_tail.next
		sublist_parent.next, sublist_tail.next, temp.next = \
				temp, temp.next, sublist_parent.next
	return dummy.next

print_linked_list(reverse_sublist(c, 3, 5))

def overlapping_no_cycle_lists(L1, L2):
	n1, n2 = L1, L2
	tail1 = tail2 = None
	while (not tail1 or not tail2) or (tail1 is tail2):
		print(n1.data, n2.data)
		if n1.next is None:
			tail1 = n1
			n1 = L2
		else:
			n1 = n1.next
		if n2.next is None:
			tail2 = n2
			n2 = L1
		else:
			n2 = n2.next
		if n1 is n2:
			return n1
	return None


c2 = ListNode(100)
c1 = ListNode(99, c2)
c = ListNode(98, c1)

a4 = ListNode(9, c)
a3 = ListNode(4, a4)
a2 = ListNode(3, a3)
a1 = ListNode(-3, a2)
a = ListNode(-10, a1)

b2 = ListNode(5, c)
b1 = ListNode(-2, b2)
b = ListNode(-10, b1)

d5 = ListNode(99)
d4 = ListNode(9, d5)
d3 = ListNode(4, d4)
d2 = ListNode(3, d3)
d1 = ListNode(-3, d2)
d = ListNode(-10, d1)

assert c == overlapping_no_cycle_lists(a,b)
assert overlapping_no_cycle_lists(a, d) is None


def delete_kth_last_node(L, k):
	'''
	:type L: ListNode
	:type k: int
	:rtype L with kth-last element removed
	'''
	# assume no cycle
	# assume k is valid (ie at least k elements in linked list)
	sentinel = ListNode()
	sentinel.next = L
	# look ahead pointer is k-step ahead of node to be deleted
	look_ahead = L
	for _ in range(k):
		look_ahead = look_ahead.next
	# iter.next is the node to be deleted
	iter = sentinel
	while look_ahead.next:
		# iterate until look_ahead is the tail, then iter.next
		# is the k-th node to be deleted
		iter = iter.next
		look_ahead = look_ahead.next
	# iter.next is node to be deleted
	iter.next = iter.next.next
	return sentinel.next


c2 = ListNode(100)
c1 = ListNode(99, c2)
c = ListNode(98, c1)

a4 = ListNode(9, c)
a3 = ListNode(4, a4)
a2 = ListNode(3, a3)
a1 = ListNode(-3, a2)
a = ListNode(-10, a1)
print_linked_list(a)
delete_kth_last_node(a, 4)
print_linked_list(a)
delete_kth_last_node(a, 0)
print_linked_list(a)
delete_kth_last_node(a, 1)
print_linked_list(a)




def remove_duplicates_from_sorted_list(L):
	# at current node, deleted next node while it's duplicate
	# then, advance to next node
	# repeat until no more next nodes
	it = L
	while it:
		next_unique = it.next
		while next_unique and it.data == next_unique.data:
			# next node is duplicate, delete
			next_unique = next_unique.next
		# deleted all duplicates at current node, advance to next node
		it.next = next_unique
		it = next_unique
	return L

	dummy = ListNode()
	dummy.next = L
	while L:
		while L.next and L.data == L.next.data:
			# next node is duplicate, delete
			L.next = L.next.next
		# deleted all duplicates at current node, advance to next node
		L = L.next
	return dummy.next

L = None
for i in reversed(range(22)):
	L = ListNode(i // 3, L)
print_linked_list(L)
print('After de-duplication -> ', end='')
remove_duplicates_from_sorted_list(L)
print_linked_list(L)
print('Done!')

def right_shift(L, k):
	'''Right shift linked list L to the right by k'''
	# first convert L to a circular linked list
	head = tail = L
	n = 1
	while tail.next:
		n += 1
		tail = tail.next
	# shift to the right by k steps is the same as
	# shift to the left by n - k steps
	k %= n
	if k == 0:
		return L
	tail.next = head
	for _ in range(n - k):
		head = head.next
		tail = tail.next
	# detach head from tail
	tail.next = None
	return head

def generate_linked_list(iter):
	'''Generate linked list from iterable'''
	head = None
	for val in reversed(iter):
		head = ListNode(val, head)
	return head

a = generate_linked_list(range(12))
print_linked_list(a)
a = right_shift(a, 12)
print_linked_list(a)

def even_odd_merge(L):
	'''
	Re-arrange L so even nodes come before odd nodes
	'''
	dummy_even_head = ListNode()
	dummy_odd_head = ListNode
	# alternate and append even or odd node to appropriate head
	even_tail = dummy_even_head
	odd_tail = dummy_odd_head
	is_even = True # assume indexing starts at 0 like arrays
	while L:
		if is_even:
			even_tail.next = L
			even_tail = even_tail.next
		else: # is odd node
			odd_tail.next = L
			odd_tail = odd_tail.next
		L = L.next
		is_even = not is_even
	# attach odd list to end of even list
	even_tail.next = dummy_odd_head.next
	return dummy_even_head.next
		
a = generate_linked_list(range(12))
print_linked_list(a)
a = even_odd_merge(a)
print_linked_list(a)

def list_pivoting(L, p):
	'''Partition L so nodes with value less than p comes before p, and nodes with
	value greater than p comes after p
	'''
	# create 3 linked list to store the three partitions
	# constant space since reusing existing nodes
	less_head = less_iter = ListNode()
	equal_head = equal_iter = ListNode()
	greater_head = greater_iter = ListNode()
	# iterate through list and append node to appropriate lists
	while L:
		if L.data < p:
			less_iter.next = L
			less_iter = less_iter.next
		elif L.data > p:
			greater_iter.next = L
			greater_iter = greater_iter.next
		else: # equal to p
			equal_iter.next = L
			equal_iter = equal_iter.next
		# process next node
		L = L.next
	# join the three partitions
	greater_iter.next = None
	equal_iter.next = greater_head.next
	less_iter.next = equal_head.next
	return less_head.next


a = generate_linked_list([random.randint(0, 10) for _ in range(20)])
print_linked_list(a)
a = list_pivoting(a, 6)
print_linked_list(a)