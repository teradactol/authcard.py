from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long
from Crypto.Random import get_random_bytes

delim = ":"

def decryptText(opts={}):

    _hash = opts.get('hash',"")
    hash_tokens = _hash.split(delim)

    passwd = opts.get('pass',"")
    # Password should be 32 characters long exactly!
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

def encryptText(opts={}):

    text = opts.get('text',"")
    text_bytes = bytes(text,'utf-8')
    
    passwd = opts.get('pass',"")
    # Password should be 32 characters long exactly!
    passwd_bytes = bytes(passwd,'utf-8')

    iv_bytes = get_random_bytes(16)
    iv_hex = iv_bytes.hex()

    counter = Counter.new(128, initial_value = bytes_to_long(iv_bytes))

    cipher = AES.new(passwd_bytes, AES.MODE_CTR, counter = counter)

    encrypted_bytes = cipher.encrypt(text_bytes)
    encrypted_hex = encrypted_bytes.hex()

    hash = iv_hex + delim + encrypted_hex
    return hash