def caesar_cipher(offset, plaintext):
    offset = offset % 26

    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            ascii_code = (ord(char) - ascii_offset + offset) % 26 + ascii_offset

            ciphertext += chr(ascii_code)
        else:
            ciphertext += char

    return ciphertext

offset = int(input("Enter value of offset: "))
plaintext = input("Enter open text: ")

ciphertext = caesar_cipher(offset, plaintext)
print("Cipher text: ", ciphertext)