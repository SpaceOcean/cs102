def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    for i in range(len(plaintext)):
        if (('X' <= plaintext[i] <= 'Z') or ('x' <= plaintext[i] <= 'z')):
            ciphertext += chr(ord(plaintext[i]) - 23)
        elif '!' <= plaintext[i] <= '@':
            ciphertext += plaintext[i]
        else:
            ciphertext += chr(ord(plaintext[i]) + 3)

    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    for i in range(len(ciphertext)):
        if ('A' <= ciphertext[i] <= 'C') or ('a' <= ciphertext[i] <= 'c'):
            plaintext += chr(ord(ciphertext[i]) + 23)
        elif '!' <= ciphertext[i] <= '@':
            plaintext += ciphertext[i]
        else:
            plaintext += chr(ord(ciphertext[i]) - 3)

    return plaintext

if __name__ == "__main__":
    entered_plaintext = input("Введите строку, которую следует закодировать: ")
    print(encrypt_caesar(entered_plaintext))
    print(decrypt_caesar(encrypt_caesar(entered_plaintext)))
