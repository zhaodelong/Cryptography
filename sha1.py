import hashlib
from string import *

m = hashlib.sha1()
in_str = "113800046"
print(in_str)
m.update(str(in_str))
hex_hash = m.hexdigest()
print(hex_hash)
print(hex_hash[0])
#print(str(m.digest()))
print("block size: ", m.block_size)
print("digest size: ", m.digest_size)

ascii_all = ascii_letters + digits
for i in ascii_all:
	in_str = "113800046"
	in_str = in_str + i
	m.update(str(in_str))
	hex_hash = m.hexdigest()
	#print(in_str)
	#print(hex_hash)
	#print(hex_hash[0])
	if (hex_hash[0] == "0"):
		print(in_str)
		print(hex_hash)
		print(hex_hash[0])