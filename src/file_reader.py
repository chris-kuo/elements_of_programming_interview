filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in py_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birtyday doesn't appear in the first million digits of pi... :(")