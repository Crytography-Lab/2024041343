def create_matrix(key):
    key = key.lower().replace("j", "i")

    alphabet = "abcdefghiklmnopqrstuvwxyz"
    letters = ""

    for char in key + alphabet:
        if char not in letters:
            letters += char

    matrix = [letters[i:i+5] for i in range(0, 25, 5)]

    return matrix


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


def encryption(plain_text, key):

    matrix = create_matrix(key)

    plain_text = plain_text.lower().replace("j", "i")

    # Add x between repeated letters
    prepared_text = ""
    i = 0

    while i < len(plain_text):

        if i + 1 < len(plain_text) and plain_text[i] == plain_text[i + 1]:
            prepared_text += plain_text[i] + "x"
            i += 1
        else:
            prepared_text += plain_text[i]
            i += 1

    # If length is odd, add x
    if len(prepared_text) % 2 != 0:
        prepared_text += "x"

    cipher_text = ""

    for i in range(0, len(prepared_text), 2):

        a = prepared_text[i]
        b = prepared_text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            cipher_text += matrix[r1][(c1 + 1) % 5]
            cipher_text += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher_text += matrix[(r1 + 1) % 5][c1]
            cipher_text += matrix[(r2 + 1) % 5][c2]

        else:
            cipher_text += matrix[r1][c2]
            cipher_text += matrix[r2][c1]

    print(f"Here is the text after the encryption: {cipher_text}")


def decryption(cipher_text, key):

    matrix = create_matrix(key)

    plain_text = ""

    for i in range(0, len(cipher_text), 2):

        a = cipher_text[i]
        b = cipher_text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            plain_text += matrix[r1][(c1 - 1) % 5]
            plain_text += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            plain_text += matrix[(r1 - 1) % 5][c1]
            plain_text += matrix[(r2 - 1) % 5][c2]

        else:
            plain_text += matrix[r1][c2]
            plain_text += matrix[r2][c1]

    print(f"Here is the text after the decryption: {plain_text}")


wanna_end = False

while not wanna_end:

    what_to_do = input(
        "Type 'encrypt' for encryption, Type 'decrypt' for decryption:\n"
    )

    text = input("Type your message:\n").replace(" ", "")
    key = input("Enter the key:\n")

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