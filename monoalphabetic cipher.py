alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

key = ['q','w','e','r','t','y','u','i','o','p','a','s','d',
       'f','g','h','j','k','l','z','x','c','v','b','n','m']


def encryption(plain_text):
    cipher_text = ""

    for char in plain_text:
        position = alphabet.index(char)
        cipher_text += key[position]

    print(f"Here is the text after the encryption: {cipher_text}")


def decryption(cipher_text):
    plain_text = ""

    for char in cipher_text:
        position = key.index(char)
        plain_text += alphabet[position]

    print(f"Here is the text after the decryption: {plain_text}")


wanna_end = False

while not wanna_end:

    what_to_do = input(
        "Type 'encrypt' for encryption, Type 'decrypt' for decryption:\n"
    )

    text = input("Type your message:\n").lower()

    if what_to_do == 'encrypt':
        encryption(plain_text=text)

    elif what_to_do == 'decrypt':
        decryption(cipher_text=text)

    play_again = input(
        "Type 'yes' to continue or 'no' to exit:\n"
    ).lower()

    if play_again == 'no':
        wanna_end = True
        print("Goodbye!")