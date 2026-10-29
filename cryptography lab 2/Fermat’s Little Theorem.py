a = int(input("Enter a:"))
p = int(input("Enter the prime number p:"))

if a % p == 0:
    print("a is divisible by p, so the theorem does not apply")
else:
    result = pow(a, p - 1, p)
    print("Result:", result)

    if result == 1:
        print("Fermat's little theorem is verified.")
    else:
        print("The theorem is not verified.")