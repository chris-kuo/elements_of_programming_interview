def phone_mnemonics(number):
	MAPPING = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO',
			   'PQSR', 'TUV', 'WXYZ']

	def partial_mnemonic_helper(digit):
		if len(number) == digit:
			mnemonics.append(''.join(partial_mnemonic))
		else:
			for c in MAPPING[int(number[digit])]:
				partial_mnemonic[digit] = c
				# generate remaining partial mnemonic
				partial_mnemonic_helper(digit + 1)

	mnemonics = []
	partial_mnemonic = [''] * len(number)
	partial_mnemonic_helper(0)

	return mnemonics

print(phone_mnemonics('34150'))
