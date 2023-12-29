import random

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def list_prime(num):
    prime_list = []
    for i in range(2, num):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

def generate_prime(bits):
    num = random.getrandbits(bits)
    return prime_number_list[num % len(prime_number_list)]

# Generate public and private keys
def generate_keys(bits):
    p = generate_prime(bits)
    print(f"p={p}")
    q = generate_prime(bits)
    print(f"q={q}")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Encrypt a message
def encrypt(public_key, message):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

# Decrypt a message
def decrypt(private_key, encrypted):
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted]
    return ''.join(decrypted)


if __name__ == '__main__':
    prime_number_list = list_prime(10000)
    public_key, private_key = generate_keys(1024)
    message = input("Enter your message:")
    encrypted_message = encrypt(public_key, message)
    # print the value of e
    print("e:", public_key[0])
    print("Encrypted:", encrypted_message)
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted:", decrypted_message)
