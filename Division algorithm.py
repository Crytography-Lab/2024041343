dividend = int(input("Enter the dividend:"))
divisor = int(input("Enter the divisor:"))

quotient = dividend // divisor
remainder = dividend % divisor

print("quotient:", quotient)
print("remainder:", remainder)
print(f"{dividend} = {divisor} * {quotient} + {remainder}")
