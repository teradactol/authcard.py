from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long

delim = ":"

def decryptText(opts={}):
    _hash = opts.get('hash',"")
    hash_tokens = _hash.split(delim)

    passwd = opts.get('pass',"")
    passwd_bytes = bytes(passwd,'utf-8')
    
    iv = hash_tokens[0]
    iv_bytes = bytes.fromhex(iv)

    hash = hash_tokens[1]
    hash_bytes = bytes.fromhex(hash)

    counter = Counter.new(128, initial_value = bytes_to_long(iv_bytes))
    cipher = AES.new(passwd_bytes, AES.MODE_CTR, counter = counter)

    decrypted_bytes = cipher.decrypt(hash_bytes)
    decrypted_text = decrypted_bytes.decode("utf-8")

    return decrypted_text