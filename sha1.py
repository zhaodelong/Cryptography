import hashlib
from string import *

m = hashlib.sha1()
in_str = "113800046"
print(in_str)
m.update(in_str)
hex_hash = m.hexdigest()
print(hex_hash)
print(hex_hash[0])
#print(str(m.digest()))
#print("block size: ", m.block_size)
#print("digest size: ", m.digest_size)

ascii_all = ascii_letters + digits
found = False
while(not found):
	for i in ascii_all:		
		m.update(i)
		in_str = in_str + i;
		hex_hash = m.hexdigest()
		#print(in_str)
		#print(hex_hash)
		#print(hex_hash[0])
		if (hex_hash[0] == "0" and hex_hash[1] == "0" and hex_hash[2] == "0" and hex_hash[3] == "0"):
			print(in_str)
			print(hex_hash)
			found = True
			break
		


