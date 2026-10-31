def rc4(data,key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    result = []
    for char in data:
        i = (i+1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        result.append(char ^ k)

    return bytes(result)

message = input("Enter the plaintext:")
key = input("Enter the secret key")
if not key:
    print("Key cannot be empty!")
else:
    encrypted = rc4(message.encode(),key.encode())
    print("Encrypted text:", encrypted.hex())
    decrypted = rc4(bytes.fromhex(encrypted.hex()),key.encode())
    print("Decrypted text:", decrypted.decode())