# function to encrypt using Caesar Cipher
def encrypt(plaintext, key):
    # remove spaces from plaintext
    plaintext = plaintext.replace(" ", "")

    # convert full stop to 'X'
    plaintext = plaintext.replace(".", "X")

    # convert to uppercase
    plaintext = plaintext.upper()

    # initialize space for ciphertext
    ciphertext = ""

    # iterate over each letter in plaintext
    for letter in plaintext:
        if letter.isalpha():
            # shift letter by key
            shifted = chr((ord(letter) - 65 + key) % 26 + 65)
            ciphertext += shifted
        else:
            ciphertext += letter

    return ciphertext


# function to decrypt using Caesar Cipher
def decrypt(ciphertext, key):
    # initialize plaintext
    plaintext = ""

    # iterate over each letter in ciphertext
    for letter in ciphertext:
        if letter.isalpha():
            # shift letter by -key
            shifted = chr((ord(letter) - 65 - key) % 26 + 65)
            plaintext += shifted
        else:
            plaintext += letter

    # convert 'X' back to full stop
    plaintext = plaintext.replace("X", ".")

    return plaintext


# main program
try:
    # accept plaintext string
    plaintext = input("Enter plaintext message: ")

    # accept cipher key
    key = int(input("Enter cipher key: "))

    # encrypt plaintext using key
    ciphertext = encrypt(plaintext, key)

    # print ciphertext
    print("Ciphertext: " + ciphertext)

    # decrypt ciphertext using key
    decrypted = decrypt(ciphertext, key)

    # print decrypted plaintext
    print("Decrypted plaintext: " + decrypted)
except ValueError:
    print("Error: Invalid cipher key")