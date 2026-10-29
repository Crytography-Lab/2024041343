from math import gcd

def euler_theorem(n):
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result


a = int(input("Enter a:"))
n = int(input("Enter n:"))

if gcd(a, n) == 1:
    phi = euler_theorem(n)
    result = pow(a, phi, n)
    print("Euler theorem result:", result)
    print("Euler's theorem is verified.")
else:
    print("Euler's theorem cannot be applied.")