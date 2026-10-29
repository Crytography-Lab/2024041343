alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']


def encryption(plain_text):

    key = [[3, 3],
           [2, 5]]

    cipher_text = ""

    for i in range(0, len(plain_text), 2):

        x1 = alphabet.index(plain_text[i])
        x2 = alphabet.index(plain_text[i + 1])

        y1 = (key[0][0] * x1 + key[0][1] * x2) % 26
        y2 = (key[1][0] * x1 + key[1][1] * x2) % 26

        cipher_text += alphabet[y1]
        cipher_text += alphabet[y2]

    print(f"Here is the text after the encryption: {cipher_text}")


def decryption(cipher_text):

    # Inverse of key matrix [[3,3],[2,5]]
    inverse_key = [[15, 17],
                   [20, 9]]

    plain_text = ""

    for i in range(0, len(cipher_text), 2):

        x1 = alphabet.index(cipher_text[i])
        x2 = alphabet.index(cipher_text[i + 1])

        y1 = (inverse_key[0][0] * x1 +
              inverse_key[0][1] * x2) % 26

        y2 = (inverse_key[1][0] * x1 +
              inverse_key[1][1] * x2) % 26

        plain_text += alphabet[y1]
        plain_text += alphabet[y2]

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