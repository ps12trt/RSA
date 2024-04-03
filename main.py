import random

def gcd(a, b):
    # PGDC (récursif)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def is_prime(n, k=40):
    # Test de primalité de Miller-Rabin
    # n -> nombre à tester
    # k -> nombre de fois à essayer le test de primalité

    # si le nombre est 2, il est premier
    if n == 2:
        return True

    # si le nombre est pair et plus grand que 2, le nombre n'est pas premier
    if n % 2 == 0 and n > 2:
        return False

    s = 0
    t = n - 1

    while t % 2 == 0:
        s += 1
        t = t // 2
    # n - 1 = 2**s*t

    for i in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(s):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    # Le nombre est probablement premier
    return True

def random_prime_number(dg):
    # Genère un nombre premier de grandeur dg
    min = 1
    max = 10**dg
    n = random.randint(min, max)
    if n % 2 == 0:
        n -= 1
    while True :
        if is_prime(n, 40):
            return n
        n += 2

def create_public_exponent(phi):
    # Genère l'exposant de chiffrement
    while True:
        e = random_prime_number(5)
        # l'exposant est strictement infériereur à phi et plus grand que 1 et est premier avec phi
        if 1 < e < phi and gcd(e, phi) == 1:
            return e

# Clé publique (données partageable) -> n, e
# Clé privée (données non partageable) -> p, q, phi


def CreatePrivateKey(e, phi):
    d = pow(e, -1, phi)
    return d

def privatekey_to_pem():
    header = "-----BEGIN RSA PRIVATE KEY-----\n"
    footer = "\n-----END RSA PRIVATE KEY-----"

def publickey_to_pem():
    header = "-----BEGIN RSA PRIVATE KEY-----\n"
    footer = "\n-----END RSA PRIVATE KEY-----"

def Encrypt(message, e, n):
    x = pow(message, e, n)
    return x

def Decrypt(x, d, n):
    message = pow(x, d, n)
    return message



p = random_prime_number(300)
q = random_prime_number(300)
n = p * q
phi = (p-1)*(q-1)
e = create_public_exponent(phi)



print(f"p:{p}")
print("---------------------")
print(f"q:{q}")
print("---------------------")
print(f"n:{n}")
print("---------------------")
print(f"phi:{phi}")
print("---------------------")
print(f"e:{e}")
