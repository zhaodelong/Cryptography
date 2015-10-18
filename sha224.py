from string import *
import hashlib
import sys

if sys.version_info < (3, 4):
	import sha3

m = hashlib.sha3_512()
in_str = ""
print(in_str)
m.update(in_str)
hex_hash = m.hexdigest()
print(hex_hash)
print(hex_hash[0])