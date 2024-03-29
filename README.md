# Cryptography
CS5153 Network Security Projects

CS5153 Midterm 
Oct 22

1. Consider a permutation cipher over the alphabet {0,1,2,3,4,6,7,8,9} and of block length 8. Suppose that we learn that the message (0,1,0,2,0,4,9,7) is encrypted to (0,7,0,2,9,1,0,4) and the message (1,3,2,4,3,5,5,5) is encrypted to (2,5,1,4,5,3,3,5).
	(a) Recover the encrypt key and express it as a matrix.
	(b) Decrpyt the ciphertext (1,3,4,8,3,0,5,6)
	(c) Remove the first digit of your Student ID, treat the rest digits as a plaintext and encrypt it.
	(d) Remove the first digit of your student ID, treate the rest as ciphertext for this cipher, and decrypt it.
	(e) Use this example to explain the weakness of a permutation cipher.

2. Create a text file that contains your name and ID number. Then computer the SHA1 hash of the file. (If you use linux, the shell command to compute SHA1 hash is sha1sum.)
	Do you believe that there is another file somewhere on some computer that has the same hash value but has different content? Why?
	Change one digit of the ID number, and recompute the SHA1 hash value.

3. Define SHA1TRUN(x) to be the hash function that takes the first two bytes of the SHA1(x). Find one ASCII string that have the SHA1TRUN hash value zero. The string should start with your ID number (in ASCII encoding). There are many implementations of the SHA1 hash function. The documentation for SHA1 in Python can be found at:
http://docs.python.org/library/sha.html

4. Define SHA3_224TRUNk to be the hash function that outputs the first k bits of the SHA3_224 function. Find two different ASCII strings that have the same SHA3_224TRUNk hash value for some k. Both of the strings should start with your OU 4x4 name (in capital letters). Your grade depends on how large k you can manage to reach. You are allowed to use any online implementations of the SHA3_224 hash function, as long as you specify the source.

