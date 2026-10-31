# RSA Encryption

p = int(input("Enter 1st prime no"))
q = int(input("Enter 2nd prime no"))
n = p*q
e = int(input("Enter public key e"))
msg = int(input("Enter message(numbers)"))
cipher = pow(msg,e,n)

print("public key is",(e,n))
print("Encrypted message is",cipher)


# RSA Decryption

p = int(input("Enter 1st prime no"))
q = int(input("Enter 2nd prime no"))
n = p*q
phi = (p-1)*(q-1)
d = int(input("Enter private key d:"))
cipher = int(input("Enter Encrypted message:"))
message = pow(cipher,d,n)

print("private key:",(d,n))
print("Decrypted message:",message)