# demo/sha256_hash_demo.py

import hashlib

data1 = b"Confidential message"
data2 = b"Conf1dential message"

hash1 = hashlib.sha256(data1).hexdigest()
hash2 = hashlib.sha256(data2).hexdigest()

print("[+] Hash 1:", hash1)
print("[+] Hash 2:", hash2)

if hash1 == hash2:
    print("Same hash")
else:
    print("Hashes differ")
