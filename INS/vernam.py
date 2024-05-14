def vernam_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = (key.upper() * (len(plain_text) // len(key) + 1))[:len(plain_text)]
    encrypted_text = ''.join(
        chr((ord(plain_char) + ord(key_char) - 2 * ord('A')) % 26 + ord('A'))
        for plain_char, key_char in zip(plain_text, key)
    )
    return encrypted_text

def vernam_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = (key.upper() * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]
    decrypted_text = ''.join(
        chr((ord(cipher_char) - ord(key_char)) % 26 + ord('A'))
        for cipher_char, key_char in zip(cipher_text, key)
    )
    return decrypted_text

# Example usage:
plaintext = "Hello"
key = "MONEY"

encrypted_text = vernam_encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = vernam_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
