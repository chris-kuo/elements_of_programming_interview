def valid_ip(s, segment=4):
	def is_valid_sub(substr):
		# 0 is valid, but 00, 00? are not
		return len(s) == 1 or (substr[0] != '0' and int(substr) < 256)

	ips = []
	for i in range(1, min(len(s), 4)):
		if not is_valid_sub(s[:i]):
			continue
		for j in range(i+1, min(len(s), i+4)):
			if not is_valid_sub(s[i:j]):
				continue
			for k in range(j+1, min(len(s), j+4)):
				if not is_valid_sub(s[j:k]):
					continue
				if is_valid_sub(s[k:]):
					ips.append('%s:%s:%s:%s' % (s[:i], s[i:j], s[j:k], s[k:]))
	return ips

print(valid_ip('19216811'))