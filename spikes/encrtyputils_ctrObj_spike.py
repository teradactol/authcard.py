import os
#Many thanks to https://codereview.stackexchange.com/a/181074 
dir_path = os.path.abspath(__file__ + "/../../")

#Many thanks to https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
import sys
sys.path.append(dir_path)

import authcard.encryptutils.ctr

passwd = "S62Sb.[RXFD#QCRx7n63A*C:ZzkaS7N;"
obj = {"hello":"world"}

obj_enc = authcard.encryptutils.ctr.encryptObj({"obj":obj,"pass":passwd})
print(obj_enc)

obj_dec = authcard.encryptutils.ctr.decryptObj({"obj":obj_enc,"pass":passwd})
print(obj_dec)

