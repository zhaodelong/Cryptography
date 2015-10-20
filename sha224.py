from string import *
from itertools import *
import sha3             #https://github.com/bjornedstrom/python-sha3


dict = {}

#ascii_all = "abcd"
ascii_all = ascii_letters + digits
found = False
nchar = 14
for i in range(len(ascii_all)):	
	if found:
		break
	print("Elements for permutation " + str(i + 1))
	permut = permutations(ascii_all, i + 1)
	permut = list(map("".join, permut))
	print("Number of permutations: " + str(len(permut)))
	for x in permut:
		in_str = "zhao0046"
		in_str = in_str + x
		m = sha3.SHA3224()
		m.update(in_str)
		hex_hash = m.hexdigest()
		hex_hash = hex_hash[0:nchar]	
		#print(in_str)
		#print(hex_hash)
		if hex_hash in dict:
			print in_str
			print hex_hash
			print dict[hex_hash]
			found = True
			break
		dict[hex_hash] = in_str
		in_str = "zhao0046"

print("Finished")


