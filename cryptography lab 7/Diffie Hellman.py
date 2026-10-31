p = int(input("Enter prime no"))
g = int(input("Enter primitive root"))
a = int(input("Enter Alice private key:"))
b = int(input("Enter Bob's private key"))

A = pow(g,a,p)
B = pow(g,b,p)

print("Alice public key:",A)
print("Bob public key:",B)

key_Alice = pow(B,a,p)
key_Bob = pow(A,b,p)

print("Alice shared key:",key_Alice)
print("Bob shared key:",key_Bob)

if key_Alice == key_Bob:
    print("Key exchange successful")