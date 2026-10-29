a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD:", a)