import os
#Many thanks to https://codereview.stackexchange.com/a/181074 
dir_path = os.path.abspath(__file__ + "/../../")

#Many thanks to https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
import sys
sys.path.append(dir_path)

import authcard.encryptutils.ctr
import authcard.encryptutils.bcrypt

passwd = "S62Sb.[RXFD#QCRx7n63A*C:ZzkaS7N;"
hash = "65e68599e50a287e9cff5dbe5818af14:653fecf2c33bc6"
decrypted_text = authcard.encryptutils.ctr.decryptText({"hash":hash,"pass":passwd})

print(decrypted_text)