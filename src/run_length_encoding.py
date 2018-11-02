import itertools

def decode(s):
	'''decode run-length-encoding (RLE) string'''
	result = []
	count = 0
	for c in s:
		if c.isdigit():
			count = count * 10 + int(c)
		elif c.isalpha():
			result.append(c * count)
			count = 0 # reset
	return ''.join(result)

def encode(s):
	'''encode s into RLE, assuming no number and only letters in string'''
	groups = itertools.groupby(s)
	result = []
	for key, group in groups:
		result.append(str(len(list(group))) + key)
	return ''.join(result)

print(encode('aaaabcccaa'))
print(decode('4a1b3c2a'))
s = 'fjaeifFFeLAAAaaaccFFeaOLOOOLhw'
t = encode(s)
assert s == decode(t)