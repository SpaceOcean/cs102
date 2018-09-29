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

    for i in range (len(plaintext)):
        if ('x' <= plaintext[i] <= 'z') or ('X' <= plaintext[i] <= 'Z'): 
            ciphertext += chr(ord(plaintext[i])-23)
        elif ('э' <= plaintext[i] <= 'я') or ('Э' <= plaintext[i] <= 'Я'):
            ciphertext += chr(ord(plaintext[i])-29)
        elif (('A' >= plaintext[i] < 'X') or ('a' >= plaintext[i] < 'x')):
            ciphertext += chr(ord(plaintext[i])+3)
        elif ('А' >= plaintext[i] < 'Э') or ('а' >= plaintext[i] < 'э'):
            ciphertext += chr(ord(plaintext[i])+3)  
        else:
            ciphertext += plaintext[i] 

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

    for i in range (len(ciphertext)):
        if ('A' <= ciphertext[i] <= 'C') or ('a' <= ciphertext[i] <= 'c'): 
            plaintext += chr(ord(ciphertext[i])+23)
        elif ('А' <= ciphertext[i] <= 'В') or ('а' <= ciphertext[i] <= 'в'):
            plaintext += chr(ord(ciphertext[i])+29)
        elif ('C' > ciphertext[i] <='Z') or ('c' > ciphertext[i] <='z'):
            plaintext += chr(ord(ciphertext[i])-3)
        elif ('В' > ciphertext[i] <='Я') or ('в' > ciphertext[i] <='я'):
            plaintext += chr(ord(ciphertext[i])-3)
        else:
            plaintext += ciphertext[i]

    return plaintext

if __name__ == "__main__":
    ciphertext = encrypt_caesar(input ("Введите строку, которую следует закодировать: "))
    print(ciphertext)
    plaintext = decrypt_caesar(ciphertext)
    print(plaintext)