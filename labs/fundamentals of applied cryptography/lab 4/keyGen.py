from random import randrange

from cryptomath import generatePrime, primitive_root, find_mod_inverse, co_prime_number


def keyGen(keySize: int) -> tuple[tuple[int, int, int, int], int]:
    p = generatePrime(keySize)
    g = primitive_root(p)
    #x = randrange(3, p)
    x = co_prime_number(p)
    while x < 3:
        x = co_prime_number(p)
    y = pow(g, x, p)

    public_key = (y, g, p)
    private_key = x

    return public_key, private_key
