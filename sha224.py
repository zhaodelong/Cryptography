from string import *
import sha3 #https://github.com/bjornedstrom/python-sha3
m = sha3.SHA3224()
print(m.name, m.digest_size)
in_str = ""
print(in_str)
m.update(in_str)
hex_hash = m.hexdigest()
print(hex_hash)
print(hex_hash[0])