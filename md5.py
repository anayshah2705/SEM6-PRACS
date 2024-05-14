def F(X, Y, Z):
    return (X & Y) | ((~X) & Z)

def G(X, Y, Z):
    return (X & Z) | (Y & (~Z))

def H(X, Y, Z):
    return X ^ Y ^ Z

def I(X, Y, Z):
    return Y ^ (X | (~Z))

def left_rotate(x, n):
    return ((x << n) & 0xFFFFFFFF) | (x >> (32 - n))

def md5(message):
    S = [7, 12, 17, 22,
         5, 9, 14, 20,
         4, 11, 16, 23,
         6, 10, 15, 21]
    K = [
        0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
        0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
        0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
        0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
        0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
        0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
        0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
    ]

    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476

    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        M = [int.from_bytes(chunk[j:j + 4], 'little') for j in range(0, 64, 4)]
        AA, BB, CC, DD = A, B, C, D

        for j in range(64):
            if 0 <= j < 15:
                F_func = F(BB, CC, DD)
                g = j
            elif 16 <= j < 31:
                F_func = G(BB, CC, DD)
                g = (5 * j + 1) % 16
            elif 32 <= j < 47:
                F_func = H(BB, CC, DD)
                g = (3 * j + 5) % 16
            elif 48<= j <= 63:
                F_func = I(BB, CC, DD)
                g = (7 * j) % 16

            temp = DD
            DD = CC
            CC = BB
            BB = (BB + left_rotate((AA + F_func + K[j] + M[g]) & 0xFFFFFFFF, S[j % 4])) & 0xFFFFFFFF
            AA = temp

        A = (A + AA) & 0xFFFFFFFF
        B = (B + BB) & 0xFFFFFFFF
        C = (C + CC) & 0xFFFFFFFF
        D = (D + DD) & 0xFFFFFFFF

    hash_result = (A.to_bytes(4, 'little') +
                   B.to_bytes(4, 'little') +
                   C.to_bytes(4, 'little') +
                   D.to_bytes(4, 'little'))
    return hash_result.hex()

# Example usage
input_string = "Hello, World!"
md5_hash = md5(input_string.encode('utf-8'))
print("MD5 hash:", md5_hash)
