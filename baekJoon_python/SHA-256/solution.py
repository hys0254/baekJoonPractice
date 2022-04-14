from hashlib import sha256
import hashlib


s=input()
s=hashlib.sha256(s.encode())
print(s.hexdigest())