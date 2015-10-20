import hashlib
from string import *
from itertools import *

found = False
ascii_all = ascii_letters + digits
for i in range(len(ascii_all)):
	if found:
		break
	print("Elements for permutation " + str(i + 1))
	permut = permutations(ascii_all, i + 1)
	permut = list(map("".join, permut))
	print("Number of permutations: " + str(len(permut)))
	for x in permut:
		in_str = "113800046"
		in_str = in_str + x
		m = hashlib.sha1()
		m.update(in_str)
		hex_hash = m.hexdigest()	
		if (hex_hash[0] == "0" and hex_hash[1] == "0" and hex_hash[2] == "0" and hex_hash[3] == "0"):
			print(in_str)
			print(hex_hash)
			found = True
			break
		in_str = "113800046"

print("Finished")
