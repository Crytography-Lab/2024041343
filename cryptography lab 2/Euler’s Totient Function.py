def euler_totient(n):
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


n = int(input("Enter the number you want:"))
print("Euler totient:", euler_totient(n))