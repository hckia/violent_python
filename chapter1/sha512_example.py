#this example shows how to use the SHA-512 hashing algorithm.
#crack_pass_sha512.py will be created, and dictionary.txt will be modified to include the new password. password.txt will include the sha512 password. under a new user.
import hashlib

epicpass = hashlib.sha512("thisIsAnEPICPassw0rd").hexdigest()

print epicpass
