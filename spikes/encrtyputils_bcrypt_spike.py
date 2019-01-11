import os
#Many thanks to https://codereview.stackexchange.com/a/181074 
dir_path = os.path.abspath(__file__ + "/../../")

#Many thanks to https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
import sys
sys.path.append(dir_path)

import authcard.encryptutils.bcrypt

text = "bishaka"
hash = authcard.encryptutils.bcrypt.encryptText({"text":text})
match = authcard.encryptutils.bcrypt.compareText({"text":text,"hash":hash})

print("Hash : " + hash)
print("Match : " + str(match))