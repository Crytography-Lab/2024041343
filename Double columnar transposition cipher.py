def encrypt(text, rails):
    result = ""

    for r in range(rails):
        for i in range(r, len(text), rails * 2 - 2):
            result += text[i]

            j = i + (rails - r - 1) * 2
            if r != 0 and r != rails - 1 and j < len(text):
                result += text[j]

    return result


def decrypt(cipher, rails):
    pattern = []
    for i in range(len(cipher)):
        pattern.append(i % (2 * rails - 2))

    rows = []
    for r in range(rails):
        rows += [i for i, x in enumerate(pattern) if x == r or x == 2 * rails - 2 - r]

    text = [""] * len(cipher)

    for i, pos in enumerate(rows):
        text[pos] = cipher[i]

    return "".join(text)


message = input("Enter the message: ")
rails = int(input("Enter the number of rails: "))

encrypted = encrypt(message, rails)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, rails)
print("Decrypted message:", decrypted)