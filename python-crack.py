"""
We can read this in the RFC, regarding the pop3 protocol: https://www.ietf.org/rfc/rfc1939.txt
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
user1 = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"

result = hashlib.md5(user1.encode())

print("here")
with open("rockyou.txt", errors="ignore") as f:
  # let's open the dictionary, for each line, we will try to see if the hash it generates matches our hashed value gathered in the wireshark frames.
  possiblePass=f.readlines()
  possiblePasss=[x.strip() for x in possiblePass]
  for passwo in possiblePasss:
  # check if the hash matches...
   if (hashlib.md5((user1+passwo).encode('utf-8')).hexdigest() == hashed_value):
     print("found")
     print(passwo) 
   else:
     #print("not found")
     next


print("done")
# end of program 
