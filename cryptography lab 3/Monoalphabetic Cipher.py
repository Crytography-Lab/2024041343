alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

choice = input("Encryption or Decryption? (E/D): ")
text = input("Enter text: ").upper()
key = input("Enter 26 letter key: ").upper()
result = ""

if choice.upper() == "E":
    for ch in text:
        if ch in alphabet:
            result += key[alphabet.index(ch)]
        else:
            result += ch

elif choice.upper() == "D":
    for ch in text:
        if ch in key:
            result += alphabet[key.index(ch)]
        else:
            result += ch

else:
    print("Invalid choice")

print("Result:", result)