def prepare_key(key):
    key = key.upper()
    key_matrix = [[0] * 5 for _ in range(5)]
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_chars = set()

    i, j = 0, 0
    for char in key:
        if char not in key_chars:
            key_matrix[i][j] = char
            key_chars.add(char)
            j += 1
            if j == 5:
                j = 0
                i += 1

    for char in alphabet:
        if char not in key_chars:
            key_matrix[i][j] = char
            j += 1
            if j == 5:
                j = 0
                i += 1

    return key_matrix

def find_char(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace("J","I")
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = find_char(key_matrix, char1)
        row2, col2 = find_char(key_matrix, char2)

        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.upper()
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_char(key_matrix, char1)
        row2, col2 = find_char(key_matrix, char2)

        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    key_matrix = prepare_key(key)
    ciphertext = playfair_encrypt(plaintext, key_matrix)
    decrypted_text = playfair_decrypt(ciphertext, key_matrix)

    def final_decrypted_text():
        if "I" in plaintext.upper():
            return decrypted_text.replace("J", "I")
        elif "J" in plaintext.upper():
            return decrypted_text.replace("I", "J")
        else:
            return decrypted_text


    print("Cipher text:", ciphertext)
    print("Decrypted text:", final_decrypted_text())

if __name__ == "__main__":
    main()