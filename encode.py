import cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom, remove
def filename(fn, change=1):
    args = ['.','.e_'][::change]
    return fn[::-1].replace(*args,1)[::-1]
def get_key(password):
    try:
        assert len(password) > 6
    except AssertionError:
        password += ' '*7
    iv = bytes(password[:7],'utf-16')
    sha = hashes.Hash(hashes.SHA256())
    sha.update(password.encode('utf-8'))
    return sha.finalize(), iv

def encode(file,password = 'test'):
    key, iv = get_key(password)
    aes = Cipher(algorithms.AES(key), modes.CBC(iv))
    enc = aes.encryptor()
    with open(file,'rb') as R:
        data = R.read()
        R.close()
    append_len = 256-(len(data)%256)
    ct = enc.update(data) + enc.update(bytes(append_len)) + enc.finalize()
    with open(filename(file),'wb') as W:
        W.write(ct)
        W.close()
    remove(file)


def decode(file,password = 'test'):
    key, iv = get_key(password)
    aes = Cipher(algorithms.AES(key), modes.CBC(iv))
    dec = aes.decryptor()
    with open(file, 'rb') as R:
        ct = R.read()
        R.close()
    with open(filename(file,-1), 'wb') as W:
        W.write(dec.update(ct)+dec.finalize())
        W.close()
    remove(file)
if __name__ == '__main__':
    file = input("Path: ").replace('"','')
    key = input("Pass: ")
    task = input("Encrypt or decrypt (e/d):").lower()
    if 'e' in task:
        encode(file, key)
    else:
        decode(file,key)
    input('done')
