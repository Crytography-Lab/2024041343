from pyDes import des, ECB, PAD_PKCS5
import base64

message = input("Enter message:")
key = input("Enter 8-character key:")
if len(key) != 8:
    print("Key must be 8 characters")
else:
    cipher = des(key.encode(), ECB, pad=None, padmode=PAD_PKCS5)
    encrypted = cipher.encrypt(message.encode())
    print("Encrypted message:", base64.b64encode(encrypted).decode())