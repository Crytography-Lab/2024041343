alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

choice = input("Enter E for encryption or D for decryption: ")
text = input("Enter text: ").upper()
key = input("Enter key: ").upper()
result = ""
j = 0

for ch in text:
    if ch in alphabet:
        t = alphabet.index(ch)
        k = alphabet.index(key[j % len(key)])

        if choice.upper() == "E":
            result += alphabet[(t + k) % 26]

        elif choice.upper() == "D":
            result += alphabet[(t - k) % 26]

        j += 1

    else:
        result += ch

print("Result:", result)