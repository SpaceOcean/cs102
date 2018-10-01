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

    for i in range (len(plaintext)):

        if (64<ord(keyword[i])<91):   # ключ - заглавная латинская
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i])-65)
        elif (96<ord(keyword[i])<123):   # ключ - строчная латинская
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i])-97)
        elif (1039<ord(keyword[i])<1072):   # ключ - заглавная русская
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i])-1040)
        elif (1071<ord(keyword[i])<1104):   # ключ - строчная русская
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i])-1072)

# проверяем не вышел ли закодированный символ за пределы алфавита
        id_symbol = ord(ciphertext[i])
        if (64 < id_symbol < 91) and not (64 < id_symbol <91): # для заглавных латинских
            ciphertextBUFER = ciphertext[i]
            ciphertext = ciphertext[:-1]
            ciphertext += chr(ord(ciphertextBUFER)-26)
        elif (96 < id_symbol < 123) and not (96 < id_symbol <123): # для строчных латинских
            ciphertextBUFER = ciphertext[i]
            ciphertext = ciphertext[:-1]
            ciphertext += chr(ord(ciphertextBUFER)-26)
        elif (1039 < id_symbol < 1072) and not (1039 < id_symbol <1072): # для заглавных русских
            ciphertextBUFER = ciphertext[i]
            ciphertext = ciphertext[:-1]
            ciphertext += chr(ord(ciphertextBUFER)-32)
        elif (1071 < id_symbol < 1104) and not (1071 < id_symbol <1104): # для строчных русских
            ciphertextBUFER = ciphertext[i]
            ciphertext = ciphertext[:-1]
            ciphertext += chr(ord(ciphertextBUFER)-32)
        else: # для символов
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

    for i in range (len(ciphertext)):

        if (ord(keyword[i])>64 and ord(keyword[i])<91):   # ключ - заглавная латинская
            plaintext += chr(ord(ciphertext[i]) - ord(keyword[i])+65)
        elif (96<ord(keyword[i])<123):   # ключ - строчная латинская
            plaintext += chr(ord(ciphertext[i]) - ord(keyword[i])+97)
        elif (1039<ord(keyword[i])<1072):   # ключ - заглавная русская
            plaintext += chr(ord(ciphertext[i]) - ord(keyword[i])+1040)
        elif (1071<ord(keyword[i])<1104):   # ключ - строчная русская
            plaintext += chr(ord(ciphertext[i]) - ord(keyword[i])+1072)

# проверяем не вышел ли декодированный символ за пределы алфавита
        id_symbol = ord(ciphertext[i])

        if (64 < id_symbol < 91) and not (64 < id_symbol <91): # для заглавных латинских
            plaintextBUFER = plaintext[i]
            plaintext = plaintext[:-1]
            plaintext += chr(ord(plaintextBUFER)+26)
        elif (96 < id_symbol < 123) and not (96 < id_symbol <123): # для строчных латинских
            plaintextBUFER = plaintext[i]
            plaintext = plaintext[:-1]
            plaintext += chr(ord(plaintextBUFER)+26)
        elif (1039 < id_symbol < 1072) and not (1039 < id_symbol <1072): # для заглавных русских
            plaintextBUFER = plaintext[i]
            plaintext = plaintext[:-1]
            plaintext += chr(ord(plaintextBUFER)+32)
        elif (1071 < id_symbol < 1104) and not (1071 < id_symbol <1104): # для строчных русских
            plaintextBUFER = plaintext[i]
            plaintext = plaintext[:-1]
            plaintext += chr(ord(plaintextBUFER)+32)
        else: # для символов
            plaintext = plaintext[:-1]
            plaintext += ciphertext[i]

    return plaintext

if __name__ == "__main__":
    keyword = input ("Введите слово-ключ: ")
    ciphertext = encrypt_vigenere(input("Введите строку, которую следует закодировать: "),keyword)
    print(ciphertext)
    plaintext = decrypt_vigenere(ciphertext,keyword)
    print(plaintext)


    