import sys

s = str(sys.argv[1]) # The binary number is taken as a command line argument
decimal_number = 0
i = 0
while i < len(s):
	if s[len(s)-1-i] == '1':
		total += 2 ** i
	i += 1

print decimal_number  # print decimal form of the binary number
