import math
def gcd(a, h):
    temp = 0
    while True:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp
p = 3
q = 7
n = p * q
e = 2
phi = (p - 1) * (q - 1)
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e = e + 1
k = 2
d = (1 + (k * phi)) / e
msg = 12.0
print("Message data = ", msg)
# Encryption
c = pow(msg, e)
c = c % n
print("Encrypted data = ", c)
# Decryption
m = pow(c, d)
m = m % n
print("Original Message Sent = ", m)
