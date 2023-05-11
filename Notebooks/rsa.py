# Simple RSA implementation
# %% --- Imports ------------------------------------------

import random
import math
import base64
# %% --- Define Functions ------------------------------------------


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def gcd(a, b):
    # Greatest common denominator
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


def encode_int_list(data: list[int]):
    encoded_bytes = []
    for d in data:
        x1 = (d & 0x000000FF) >> 0
        x2 = (d & 0x0000FF00) >> 8
        x3 = (d & 0x00FF0000) >> 16
        x4 = (d & 0xFF000000) >> 24
        encoded_bytes.append(x1)
        encoded_bytes.append(x2)
        encoded_bytes.append(x3)
        encoded_bytes.append(x4)

    return base64.b64encode(bytes(encoded_bytes))


def decode_int_list(data: bytes):
    decoded_bytes = base64.b64decode(data)
    decoded_ints = []
    for i in range(0, len(decoded_bytes), 4):
        x1 = decoded_bytes[i]
        x2 = decoded_bytes[i + 1]
        x3 = decoded_bytes[i + 2]
        x4 = decoded_bytes[i + 3]
        x = x1 | (x2 << 8) | (x3 << 16) | (x4 << 24)
        decoded_ints.append(x)
    return decoded_ints


def emoji_encoding(text: str):
    alphabet = "🐔🐀🐰🐶🐛🐱🐟🐦🐳🐎🐉🐜🐒🐄🐞🐫🐍🐲🐾🐻🐂🐸🐢🐏🐼🐝🐠🐪🐥🐯🐴🐙🐡🐅🐁🐈🐓🐽🐧🐭🐣🐮️🐨🐵🐇🐬🐗🐩🐋🐤🐐🐿🐘🐕🐑🐖🐚🐊🐷🐃🐹🐌🐆🐺"
    result = []
    for c in text:
        if c.isalpha():
            if c.isupper():
                ix = ord(c) - ord('A')
            else:
                ix = ord(c) - ord('a') + 26
            result.append(alphabet[ix])
        else:
            result.append(c)

    return "".join(result)


# %% Generate the keys


def generate_rsa_keys(p, q):

    # Step 1: Choose two distinct prime numbers p and q.
    print("p: ", p)
    print("q: ", q)

    # Step 2: Compute n = pq.
    n = p * q
    print("n: ", n)

    # Step 3: Compute φ(n) = φ(p)φ(q) = (p − 1)(q − 1)
    phi = lcm(p - 1, q - 1)  # carmichals totient functions
    # Euler totient function, equivalent to lcm(p - 1, q - 1)
    phi = (p - 1) * (q - 1)
    print("phi: ", phi)

    # Step 4: Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; i.e., e and φ(n) are coprime.
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    print("e: ", e) # PUBLIC KEY

    # Step 5: Determine d as d ≡ e−1 (mod φ(n)); i.e., d is the modular multiplicative inverse of e modulo φ(n).
    d = pow(e, -1, phi)     # d = e^-1 mod phi ---> Finite Fields Algebra
    print("d: ", d) # PRIVATE KEY

    return e, d, n

p = 61  # MUST BE PRIME - MUST BE SECRET
q = 53  # MUST BE PRIME - MUST BE SECRET
e, d, n = generate_rsa_keys(p, q)



# How to encrypt

# m * e mod n
# mod = %


# %% Encrypt and decrypt

msg = "Hello world" # UNICODE
print("msg: ", msg)
msg_data = bytes(msg, encoding="utf-8")


# %%
cipher_text = []
for char in msg_data:
    # char * e % n
    #encrypted_character = pow(char, e, n)
    encrypted_character = (char ** e) % n
    cipher_text.append(encrypted_character)
print("cipher_text: ", cipher_text)

# %% Decrypt
plain_text = []
for char in cipher_text:
    #decrypted_character = pow(char, d, n)
    decrypted_character = (char ** d) % n
    plain_text.append(decrypted_character)

plain_text_str = str(bytes(plain_text), encoding="utf-8")
print("plain_text: ", plain_text_str)


# %% Crack it?

# Public:  e, n
# Private: d

# n = p * q
for i in range(n): #   n = 100000000000000000000000000000000000000000
    p = i
    if is_prime(p) == True:
        if n % p == 0:
            q = n // p
            print("p = ", p)
            print("q = ", q)
            break






# %% Create a signature

msg = f"Hello world; Signed by Bob; 2021-09-30; PUBKEY {e, n}"
msg_bytes = bytes(msg, encoding="utf-8")

signature = []
for char in msg_bytes:
    signature.append(pow(char, d, n))
print("signature: ", signature)


# Verify the signature
plain_text = []
for char in signature:
    plain_text.append(pow(char, e, n))
print("plain_text: ", str(bytes(plain_text), encoding="utf-8"))

# %%
