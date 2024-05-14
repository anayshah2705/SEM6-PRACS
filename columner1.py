def single_round_encryption(pt, key):
    temp = [[]]
    index = 0
    count = 0
    for i in pt:
        if count == len(key):
            count = 0
            index += 1
            temp.append([])
        temp[index].append(i)
        count += 1
    if count != 0 and count < len(key):
        for i in range(index - 1, len(key)):
            temp[index].append('X')
    order = []
    print(temp)
    for i in key:
        order.append(i)
    order.sort()
    encrypted = ''
    for i in order:
        count = key.index(i)
        key = key.replace(i, ' ', 1)
        for j in range(index + 1):
            encrypted += temp[j][count]
        encrypted += " "
    return encrypted


def multiple_round_encryption(pt, key1, key2):
    result1 = single_round_encryption(pt, key1).replace(' ', '')
    result2 = single_round_encryption(result1, key2)
    return result2


def single_round_decryption(encryption, key):
    order = []
    for i in key:
        order.append(i)
    order.sort()
    temp = [[]]
    count = 0
    index = 0
    temp1 = 0
    for i in range(len(encryption)):
        if count == len(key):
            count = 0
            index += 1
            temp.append([])
        temp[index].append('')
        count += 1
    for i in order:
        count = key.index(i)
        key = key.replace(i, ' ', 1)
        for j in range(index + 1):
            temp[j][count] = encryption[temp1]
            temp1 += 1
    result = ''
    for i in range(index + 1):
        for j in range(len(key)):
            result += temp[i][j]
    return result


def multiple_round_decryption(encryption, key1, key2):
    result1 = single_round_decryption(encryption, key2)
    result2 = single_round_decryption(result1, key1)
    return result2


def driver():
    choice = int(input(
        "Enter\n1.Single Round Encryption\n2.Multiple Rounds Encryption\n3.Single Rounds Decryption\n4.Multiple Rounds Decryption:\n"))
    while choice != 0:
        if choice == 1:
            pt = input("Enter the plain text:").replace(' ', '')
            key1 = input("Enter the key:\n")
            result = single_round_encryption(pt, key1)
            print(f"ENCRYPTED TEXT: {result}")
        elif choice == 2:
            pt = input("Enter the plain text:").replace(' ', '')
            key1 = input("Enter the key 1:\n")
            key2 = input("Enter the key 2:\n")
            result = multiple_round_encryption(pt, key1, key2)
            print(f"ENCRYPTED TEXT: {result}")
        elif choice == 3:
            encrypted = input("Enter text to be decrypted:").replace(' ', '')
            key1 = input("Enter the key:\n")
            result = single_round_decryption(encrypted, key1).replace('X', '')
            print(f"DECRYPTED TEXT: {result}")
        elif choice == 4:
            pt = input("Enter the encrypted text:").replace(' ', '')
            key1 = input("Enter the key 1:\n")
            key2 = input("Enter the key 2:\n")
            print(f"DECRYPTED TEXT: {result}")
        else:
            print("Incorrect choice!!")
        choice = int(input(
            "Enter\n1.Single Round Encryption\n2.Multiple Rounds Encryption\n3.Single Rounds Decryption\n4.Multiple Rounds Decryption\n0.Exit:\n"))


driver()

# ATTACK TODAY AT NINE
# single_round_decryption('AKYNCAIXADNXTTAETOTX','APPLE')