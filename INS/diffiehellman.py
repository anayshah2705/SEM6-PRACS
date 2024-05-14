def prime_checker(p):
    # Checks if the number entered is a prime number or not
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1

def primitive_check(g, p, L):
    # Checks if the entered number is a primitive root or not
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
    return 1

L = []
while True:
    P = int(input("Enter P: "))
    if prime_checker(P) == -1:
        print("Number is not prime, please enter again!")
        continue
    break

while True:
    G = int(input(f"Enter the primitive root of {P}: "))
    if primitive_check(G, P, L) == -1:
        print(f"Number {G} is not a primitive root of {P}, please try again!")
        continue
    break

# Private Keys
x1 = int(input("Enter the private key of User 1: "))
x2 = int(input("Enter the private key of User 2: "))

while True:
    if x1 >= P or x2 >= P:
        print(f"Private keys of both users should be less than {P}!")
        continue
    break

# Calculate Public Keys
y1 = pow(G, x1) % P
y2 = pow(G, x2) % P

# Generate Secret Keys
k1 = pow(y2, x1) % P
k2 = pow(y1, x2) % P

print(f"Secret Key for User 1 is {k1}")
print(f"Secret Key for User 2 is {k2}")

if k1 == k2:
    print("Keys have been exchanged successfully.")
else:
    print("Keys have not been exchanged successfully.")
