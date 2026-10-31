import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# AES Encryption
def encrypt(plaintext, key):
    aes = AESGCM(key)
    nonce = os.urandom(12)

    ciphertext = aes.encrypt(nonce, plaintext.encode("utf-8"), None)

    return (nonce + ciphertext).hex()


# AES Decryption
def decrypt(ciphertext_hex, key):
    data = bytes.fromhex(ciphertext_hex)
    nonce = data[:12]
    ciphertext = data[12:]

    aes = AESGCM(key)
    plaintext = aes.decrypt(nonce, ciphertext, None)

    return plaintext.decode("utf-8")


# main program
print("AES Encryption and Decryption")

user_key = input("Enter secret key (16,24,or32 characters):")

# AES requires a key of 16,24,or32 bytes
key = user_key.encode("utf-8")

if len(key) not in (16,24,32):
    print("Error: key must be 16,24,or32 bytes long.")
else:
    plaintext = input("Enter plaintext:")
    encrypted = encrypt(plaintext, key)
    print("Encrypted text:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted text:", decrypted)