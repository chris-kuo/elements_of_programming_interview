def roman2decimal(s):
	MAPPING = {'I': 1,
			   'V': 5,
			   'X': 10,
			   'L': 50,
			   'C': 100,
			   'D': 500,
			   'M': 1000}
	# start from the right, the current digit is positive if
	# previous digit is smaller than current digit, else negative
	cum = MAPPING[s[-1]]
	for i in range(len(s) - 1):
		cum += MAPPING[s[i]] if MAPPING[s[i]] >= MAPPING[s[i+1]] else -MAPPING[s[i]]
	return cum

print(roman2decimal('III'))	
print(roman2decimal('VII'))
print(roman2decimal('XIV'))
print(roman2decimal('LIX'))
print(roman2decimal('CMDCCLIXVII'))