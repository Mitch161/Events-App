#06/08/19
#Diffie Hellman Key Exchange
from itertools import cycle
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib

class DiffieHellman():
    def __init__(self, value):
        self.n = 65537 #4000 bits
        self.g = 11 #smaller than n
        self.priv_value = value
        self.value = 0
        self.key = 0
        self.encrypted_data = None

        self.BS = 16
        self.pad = lambda s: s+(self.BS - len(s)%self.BS)*chr(self.BS-len(s)%self.BS)
        self.unpad = lambda s: s[0:-s[-1]]

    def get_value(self):
        return self.value

    def set_value(self):
        self.value = (self.g ** self.priv_value % self.n)
        
    def double_power(self, received_key):
        self.key = (received_key ** self.priv_value % self.n)

    def int_to_str(self):
        key = str(self.key)
        newkey = ""
        for number in key:
            newkey = newkey + chr(int(key))
        self.key = newkey

    def hash_key(self):
        self.int_to_str()
        self.key = hashlib.sha256(self.key.encode('utf-8')).digest()
        #hash = SHA256.new()
        #hash.update((str(self.key)).encode())
        #self.key = hash.digest()

    def encrypt(self, raw):
        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher =AES.new(self.key,AES.MODE_CBC,iv)
        return base64.b64encode(iv+cipher.encrypt(raw.encode('utf8')))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key,AES.MODE_CBC,iv)
        return self.unpad(cipher.decrypt(enc[16:]))
