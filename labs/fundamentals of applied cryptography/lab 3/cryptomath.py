import random


def isPrime(n):
    count = 0
    for i in range(2, int(n**0.5)+1):
        count += 1
        if n % i == 0:
            return False
        if count > 2000:
            return True

    return True


def generateLargePrime(keysize: int) -> int:
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if isPrime(num):
            return num


def gcd(a: int, b: int) -> int:
    while a != 0:
        a, b = b % a, a
    return b


def find_mod_inverse(a: int, m: int) -> int:
    if gcd(a, m) != 1:
        raise ValueError(f"mod inverse of {a!r} and {m!r} does not exist")
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
