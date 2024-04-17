import requests
import json
from Crypto.Cipher import AES, DES3, DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

# Encryption method


def encrypt(data, enckey, iv):

    enckey = b64decode(enckey)
    iv = b64decode(iv)

    cipher = DES3.new(enckey, DES3.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(
        pad(bytes(data, encoding='utf-8'), DES3.block_size))
    ciphertext = b64encode(ct_bytes).decode('utf-8')

    return ciphertext


# Decryption method
def decrypt(data, deckey, iv):
    try:
        deckey = b64decode(deckey)
        iv = b64decode(iv)
        data = b64decode(data)

        cipher = DES3.new(deckey, DES3.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(data), DES3.block_size)

        return pt.decode('utf-8')

    except (ValueError, KeyError):
        return 'Incorrect decryption'


# Integration variables
url = ''
enckey = ''
deckey = ''
hash = ''
action = ''
userId = ''
userName = ''
fluxo = ''

# Creating an IV
key = get_random_bytes(8)
cipher = DES.new(key, DES3.MODE_CBC)
iv = b64encode(cipher.iv).decode('utf-8')

# Encrypting data
actionEncypted = encrypt(action, enckey, iv)
userIdEncrypted = encrypt(userId, enckey, iv)
userNameEncrypted = encrypt(userName, enckey, iv)
fluxoEncrypted = encrypt(fluxo, enckey, iv)

# Creating the submission structure
request = {
    'HASH': hash,
    'ANNAEXEC': iv,
    'ACTION': actionEncypted,
    'USER_ID': userIdEncrypted,
    'USER_NAME': userNameEncrypted,
    'START_SERVICE': fluxoEncrypted
}

# Making a post for AnnA
response = requests.post(url, request)

# Retrieving AnnA's response
response = response.text

# Separating the received IV from the AnnA response string
responseEncrypted = response.split(iv)

# Decrypting the new IV
newIV = decrypt(responseEncrypted[1], enckey, iv)

# Decrypting the content of the reply
responseDecrypt = decrypt(responseEncrypted[0], deckey, newIV)

# Log
print('\n')
print('  -> Server response:\n', response)
print('  -> Separating the new IV from the json:\n', responseEncrypted)
print('  -> New IV: ', newIV)
print('  -> Decrypted return: ', responseDecrypt)
print('\n')
