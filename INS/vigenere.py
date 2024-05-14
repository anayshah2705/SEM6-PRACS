def vigenere_encrypt(plain_text, key):
    result = ""
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            # Shift the character based on the corresponding key character
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            key_index += 1
        else:
            # Preserve non-alphabetic characters
            result += char

    return result

def vigenere_decrypt(cipher_text, key):
    result = ""
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            # Shift the character based on the corresponding key character
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                result += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            key_index += 1
        else:
            # Preserve non-alphabetic characters
            result += char

    return result

# Example usage:
plaintext = "JAVATPOINT"
key = "BEST"

encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
