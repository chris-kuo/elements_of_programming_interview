def find_substring(s, sub):
	'''
	Return index of first character of first occurrence of sub.
	Return -1 if sub not in s
	'''
	def 
	
	for i in range(len(s) - len(sub) + 1):
		for j in range(len(sub)):
			found = True
			if s[i+j] != sub[j]:
				found = False
				break
		if found:
			return i
	return -1

s = 'hello world!'
sub1 = 'llo'
sub2 = 'lla'
sub3 = 'd!'

print(find_substring(s, sub1))
print(find_substring(s, sub2))
print(find_substring(s, sub3))