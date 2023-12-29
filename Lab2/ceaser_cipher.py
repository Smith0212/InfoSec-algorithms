def encrypt(text, key):
    cipher = ''
    for char in text:
        if char == ' ':
            cipher += ''
        elif char.isupper():
            cipher += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + key - 97) % 26 + 97)
    return cipher


def decrypt(text, key):
    cipher = ''
    for char in text:
        if char == ' ':
            cipher += ''
        elif char.isupper():
            cipher += chr((ord(char) - key - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) - key - 97) % 26 + 97)
    return cipher

def main():
    p_text = input("Enter text to encrypt: ")
    key = int(input("Enter key: "))
    print("Plain text: ", p_text)
    e_text = encrypt(p_text,key)
    print("encrypted text: ", e_text)
    print("decrypted text: ", decrypt(e_text,key))

if __name__=="__main__":
    main()