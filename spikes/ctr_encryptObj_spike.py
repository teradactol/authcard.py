from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long
from Crypto.Random import get_random_bytes

text = "My Text"
text_bytes = bytes(text,'utf-8')

passwd = "S62Sb.[RXFD#QCRx7n63A*C:ZzkaS7N;"
passwd_bytes = bytes(passwd,'utf-8')

iv_bytes = get_random_bytes(16)
iv_hex = iv_bytes.hex()

counter = Counter.new(128, initial_value = bytes_to_long(iv_bytes))

cipher = AES.new(passwd_bytes, AES.MODE_CTR, counter = counter)

encrypted_bytes = cipher.encrypt(text_bytes)
encrypted_hex = encrypted_bytes.hex()

hash = iv_hex + ":" + encrypted_hex

print(iv_bytes)
print(iv_hex)
print(encrypted_hex)
print(hash)