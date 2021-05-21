"""
Examples:
             S: +OK POP3 server ready <1896.697170952@dbc.mtview.ca.us>
             C: APOP mrose c4c9334bac560ecc979e58001b3e22fb
             S: +OK maildrop has 1 message (369 octets)

             In this example, the shared  secret  is  the  string  `tan-
             staaf'.  Hence, the MD5 algorithm is applied to the string

                <1896.697170952@dbc.mtview.ca.us>tanstaaf

             which produces a digest value of

                c4c9334bac560ecc979e58001b3e22fb

"""
import hashlib
import os
import sys

hashed_value = "4ddd4137b84ff2db7291b568289717f0"
user = "bsmith"
user1 = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"
aa = "aabb"
result = hashlib.md5(user1.encode())
#print(result.hexdigest())
print("here")
with open("rockyou.txt","r") as f:
  possiblePass=f.readlines()
  print("there")
  possiblePasss=[x.strip() for x in possiblePass]
  print("cumbia420")
  for passwo in possiblePasss:
	print(passwo)
  	if (hashlib.md5((user1+passwo).encode('utf-8')).hexdigest() == hashed_value):
    		print("found")
		exit()
  	else:
    		print("not found")
  

print(hashlib.md5(("aa"+"bb").encode('utf-8')).hexdigest())
print(hashlib.md5(aa.encode()).hexdigest())

