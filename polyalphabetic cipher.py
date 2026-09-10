alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']


def encryption(plain_text, key):
    cipher_text = ""

    for i in range(len(plain_text)):
        position = alphabet.index(plain_text[i])
        key_position = alphabet.index(key[i % len(key)])

        new_position = (position + key_position) % 26
        cipher_text += alphabet[new_position]

    print(f"Here is the text after the encryption: {cipher_text}")


def decryption(cipher_text, key):
    plain_text = ""

    for i in range(len(cipher_text)):
        position = alphabet.index(cipher_text[i])
        key_position = alphabet.index(key[i % len(key)])

        new_position = (position - key_position) % 26
        plain_text += alphabet[new_position]

    print(f"Here is the text after the decryption: {plain_text}")


wanna_end = False

while not wanna_end:

    what_to_do = input(
        "Type 'encrypt' for encryption, Type 'decrypt' for decryption:\n"
    )

    text = input("Type your message:\n").lower()
    key = input("Enter the key:\n").lower()

    if what_to_do == 'encrypt':
        encryption(plain_text=text, key=key)

    elif what_to_do == 'decrypt':
        decryption(cipher_text=text, key=key)

    play_again = input(
        "Type 'yes' to continue or 'no' to exit:\n"
    ).lower()

    if play_again == 'no':
        wanna_end = True
        print("Goodbye!")