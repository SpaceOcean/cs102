def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    while len(plaintext) > len(keyword):
        keyword *= 2

    ciphertext = ""

    for i in range(len(plaintext)):
        if 'A' <= keyword[i] <= 'Z':
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i]) - 65)
        elif 'a' <= keyword[i] <= 'z':
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i]) - 97)
# проверяем не вышел ли закодированный символ за пределы алфавита
        if ('A' <= plaintext[i] <= 'Z' and ciphertext[i] > 'Z'):
            ciphertext_bufer = ciphertext[i]
            ciphertext = ciphertext[:-1]
            ciphertext += chr(ord(ciphertext_bufer) - 26)
        elif ('a' <= plaintext[i] <= 'z' and ciphertext[i] > 'z'):
            ciphertext_bufer = ciphertext[i]
            ciphertext = ciphertext[:-1]
            ciphertext += chr(ord(ciphertext_bufer) - 26)
        elif '!' <= plaintext[i] <= '@': # для символов
            ciphertext = ciphertext[:-1]
            ciphertext += plaintext[i]

    return ciphertext

def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    while len(ciphertext) > len(keyword):
        keyword *= 2
    plaintext = ""

    for i in range(len(ciphertext)):
        if 'A' <= keyword[i] <= 'Z':
            plaintext += chr(ord(ciphertext[i]) - ord(keyword[i]) + 65)
        elif 'a' <= keyword[i] <= 'z':
            plaintext += chr(ord(ciphertext[i]) - ord(keyword[i]) + 97)
# проверяем не вышел ли закодированный символ за пределы алфавита
        if ('A' <= ciphertext[i] <= 'Z' and plaintext[i] < 'A'):
            plaintext_bufer = plaintext[i]
            plaintext = plaintext[:-1]
            plaintext += chr(ord(plaintext_bufer) + 26)
        elif ('a' <= ciphertext[i] <= 'z' and plaintext[i] < 'a'):
            plaintext_bufer = plaintext[i]
            plaintext = plaintext[:-1]
            plaintext += chr(ord(plaintext_bufer) + 26)
        elif '!' <= ciphertext[i] <= '@': # для символов
            plaintext = plaintext[:-1]
            plaintext += ciphertext[i]

    return plaintext

if __name__ == "__main__":
    input_word = input("Введите строку, которую следует закодировать: ")
    input_key = input("Введите слово-ключ: ")
    print(encrypt_vigenere(input_word, input_key))
    print(decrypt_vigenere(encrypt_vigenere(input_word, input_key), input_key))
