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
    ciphertext = []
    for i in range (0,len(plaintext)):
        if (ord(plaintext[i]) > 87 and ord(plaintext[i]) < 91) or (ord(plaintext[i]) > 119 and ord(plaintext[i]) < 123): # для сиволов x,y,z,X,Y,Z
            ciphertext.append(chr(ord(plaintext[i])-23))
        elif ((ord(plaintext[i]) > 1068 and ord(plaintext[i]) < 1072) or (ord(plaintext[i]) > 1100 and ord(plaintext[i]) < 1104)) or (ord(plaintext[i]) > 220 and ord(plaintext[i]) < 224) or (ord(plaintext[i]) > 252 and ord(plaintext[i]) < 256): # для сиволов э,ю,я,Э,Ю,Я
            ciphertext.append(chr(ord(plaintext[i])-29))
        elif (ord(plaintext[i]) > 64 and ord(plaintext[i]) < 88) or (ord(plaintext[i]) > 96 and ord(plaintext[i]) < 120) or (ord(plaintext[i]) > 191 and ord(plaintext[i]) < 221) or (ord(plaintext[i]) > 223 and ord(plaintext[i]) < 253) or (ord(plaintext[i]) > 1039 and ord(plaintext[i]) < 1068) or (ord(plaintext[i]) > 1071 and ord(plaintext[i]) < 1101):
            ciphertext.append(chr(ord(plaintext[i])+3))
        else:
            ciphertext.append(plaintext[i])
    print (''.join(ciphertext))   

    return ciphertext

encrypt_caesar(str(input ("Введите строку, которую следует закодировать: ")))


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
    plaintext = []
    for i in range (0,len(ciphertext)):
        if (ord(ciphertext[i]) > 64 and ord(ciphertext[i]) < 68) or (ord(ciphertext[i]) > 96 and ord(ciphertext[i]) < 100): # для сиволов a,b,c,A,B,C
            plaintext.append(chr(ord(ciphertext[i])+23))
        elif ((ord(ciphertext[i]) > 1038 and ord(ciphertext[i]) < 1043) or (ord(ciphertext[i]) > 1071 and ord(ciphertext[i]) < 1075)) or (ord(ciphertext[i]) > 162 and ord(ciphertext[i]) < 166) or (ord(ciphertext[i]) > 194 and ord(ciphertext[i]) < 198): # для сиволов а,б,в,А,Б,В
            plaintext.append(chr(ord(ciphertext[i])+29))
        elif (ord(ciphertext[i]) > 67 and ord(ciphertext[i]) < 91) or (ord(ciphertext[i]) > 99 and ord(ciphertext[i]) < 123) or (ord(ciphertext[i]) > 194 and ord(ciphertext[i]) < 224) or (ord(ciphertext[i]) > 226 and ord(ciphertext[i]) < 256) or (ord(ciphertext[i]) > 1042 and ord(ciphertext[i]) < 1071) or (ord(ciphertext[i]) > 1074 and ord(ciphertext[i]) < 1104):
            plaintext.append(chr(ord(ciphertext[i])-3))
        else:
            plaintext.append(ciphertext[i])
    print (''.join(plaintext))

    return plaintext

decrypt_caesar(str(input ("Введите строку, которую следует декодировать: ")))