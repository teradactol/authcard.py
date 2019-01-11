from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long

passwd = "S62Sb.[RXFD#QCRx7n63A*C:ZzkaS7N;"
passwd_bytes = bytes(passwd,'utf-8')

_hash = "65e68599e50a287e9cff5dbe5818af14:653fecf2c33bc6" # Should decrypt to "My Text"
hash_tokens = _hash.split(":")

iv = hash_tokens[0]
iv_bytes = bytes.fromhex(iv)

hash = hash_tokens[1]
hash_bytes = bytes.fromhex(hash)

counter = Counter.new(128, initial_value = bytes_to_long(iv_bytes))
cipher = AES.new(passwd_bytes, AES.MODE_CTR, counter = counter)

print(cipher.decrypt(hash_bytes))

# Many thanks to https://www.programcreek.com/python/example/87998/Crypto.Cipher.AES.MODE_CTR for the decryption code