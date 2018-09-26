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
    ciphertext = []

    for i in range (0,len(plaintext)):

        if (ord(keyword[i])>64 and ord(keyword[i])<91):   # ключ - заглавная латинская
            ciphertext.append(chr(ord(plaintext[i]) + ord(keyword[i])-65))
        elif (ord(keyword[i])>96 and ord(keyword[i])<123):   # ключ - строчная латинская
            ciphertext.append(chr(ord(plaintext[i]) + ord(keyword[i])-97))
        elif (ord(keyword[i])>1039 and ord(keyword[i])<1072):   # ключ - заглавная русская
            ciphertext.append(chr(ord(plaintext[i]) + ord(keyword[i])-1040))
        elif (ord(keyword[i])>1071 and ord(keyword[i])<1104):   # ключ - строчная русская
            ciphertext.append(chr(ord(plaintext[i]) + ord(keyword[i])-1072))

# проверяем не вышел ли закодированный символ за пределы алфавита

        if (ord(plaintext[i]) > 64 and ord(plaintext[i]) < 91) and not (ord(ciphertext[i])>64 and ord(ciphertext[i])<91): # для заглавных латинских
            ciphertextBUFER = ciphertext[i]
            ciphertext.pop()
            ciphertext.append(chr(ord(ciphertextBUFER)-26))
        elif (ord(plaintext[i]) > 96 and ord(plaintext[i]) < 123) and not (ord(ciphertext[i])>96 and ord(ciphertext[i])<123): # для строчных латинских
            ciphertextBUFER = ciphertext[i]
            ciphertext.pop()
            ciphertext.append(chr(ord(ciphertextBUFER)-26))
        elif (ord(plaintext[i]) > 1039 and ord(plaintext[i]) < 1072) and not (ord(ciphertext[i])>1039 and ord(ciphertext[i])<1072): # для заглавных русских
            ciphertextBUFER = ciphertext[i]
            ciphertext.pop()
            ciphertext.append(chr(ord(ciphertextBUFER)-32))
        elif (ord(plaintext[i]) > 1071 and ord(plaintext[i]) < 1104) and not (ord(ciphertext[i])>1071 and ord(ciphertext[i])<1104): # для строчных русских
            ciphertextBUFER = ciphertext[i]
            ciphertext.pop()
            ciphertext.append(chr(ord(ciphertextBUFER)-32))
        elif (ord(plaintext[i]) < 65 and ord(plaintext[i]) > 90 and ord(plaintext[i]) < 97 and ord(plaintext[i]) > 122 and ord(plaintext[i]) < 1040 and ord(plaintext[i]) > 1103): # для символов
            ciphertext.pop()
            ciphertext.append(plaintext[i])

    print ("Строка до шифрования: ", plaintext)
    print ("Строка после шифрования: ", ''.join(ciphertext))   

    return ciphertex

encrypt_vigenere(str(input ("Введите строку, которую следует закодировать: ")),str(input ("Введите слово-ключ: ")))

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
    plaintext = []

    for i in range (0,len(ciphertext)):

        if (ord(keyword[i])>64 and ord(keyword[i])<91):   # ключ - заглавная латинская
            plaintext.append(chr(ord(ciphertext[i]) - ord(keyword[i])+65))
        elif (ord(keyword[i])>96 and ord(keyword[i])<123):   # ключ - строчная латинская
            plaintext.append(chr(ord(ciphertext[i]) - ord(keyword[i])+97))
        elif (ord(keyword[i])>1039 and ord(keyword[i])<1072):   # ключ - заглавная русская
            plaintext.append(chr(ord(ciphertext[i]) - ord(keyword[i])+1040))
        elif (ord(keyword[i])>1071 and ord(keyword[i])<1104):   # ключ - строчная русская
            plaintext.append(chr(ord(ciphertext[i]) - ord(keyword[i])+1072))

# проверяем не вышел ли декодированный символ за пределы алфавита

        if (ord(ciphertext[i]) > 64 and ord(ciphertext[i]) < 91) and not (ord(plaintext[i])>64 and ord(plaintext[i])<91): # для заглавных латинских
            plaintextBUFER = plaintext[i]
            plaintext.pop()
            plaintext.append(chr(ord(plaintextBUFER)+26))
        elif (ord(ciphertext[i]) > 96 and ord(ciphertext[i]) < 123) and not (ord(plaintext[i])>96 and ord(plaintext[i])<123): # для строчных латинских
            plaintextBUFER = plaintext[i]
            plaintext.pop()
            plaintext.append(chr(ord(plaintextBUFER)+26))
        elif (ord(ciphertext[i]) > 1039 and ord(ciphertext[i]) < 1072) and not (ord(plaintext[i])>1039 and ord(plaintext[i])<1072): # для заглавных русских
            plaintextBUFER = plaintext[i]
            plaintext.pop()
            plaintext.append(chr(ord(plaintextBUFER)+32))
        elif (ord(ciphertext[i]) > 1071 and ord(ciphertext[i]) < 1104) and not (ord(plaintext[i])>1071 and ord(plaintext[i])<1104): # для строчных русских
            plaintextBUFER = plaintext[i]
            plaintext.pop()
            plaintext.append(chr(ord(plaintextBUFER)+32))
        elif (ord(ciphertext[i]) < 65 and ord(ciphertext[i]) > 90 and ord(ciphertext[i]) < 97 and ord(ciphertext[i]) > 122 and ord(ciphertext[i]) < 1040 and ord(ciphertext[i]) > 1103): # для символов
            plaintext.pop()
            plaintext.append(ciphertext[i])

    print ("Строка до дешифрования: ", ciphertext)
    print ("Строка после дешифрования: ", ''.join(plaintext)) 

    return ciphertext

decrypt_vigenere(str(input ("Введите строку, которую следует декодировать: ")),str(input ("Введите слово-ключ: ")))
    