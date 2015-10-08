import hashlib
m = hashlib.sha1()
m.update("113800046")
print(m.hexdigest())
print(str(m.digest()))
print("block size: ", m.block_size)
print("digest size: ", m.digest_size)