def sinusoidal_string(s):
	# top row: index = 1 + 4n
	# middle row: index = 2n
	# bottom row: index = 3 + 4n
	top = []
	middle = []
	bottom = []
	for i, c in enumerate(s):
		if i & 1 == 0:
			middle.append(c)
		elif i & 0b11 == 1:
			top.append(c)
		else:
			bottom.append(c)
	return ''.join([''.join(row) for row in (top, middle, bottom)])


def sinusoidal_string_with_slicing(s):
	return s[1:len(s):4] + s[:len(s):2] + s[3:len(s):4]


s = 'Hello_World!'
print(sinusoidal_string(s))
print(sinusoidal_string_with_slicing(s))