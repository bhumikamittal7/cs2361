p = 16868678779879798798798797465465479
g = 53

def extended_gcd_algo(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd_algo(b, a % b)
        return d, y, x - (a // b) * y

def inverse(g, p):
    d, x, y = extended_gcd_algo(g, p)
    if d != 1:
        raise ValueError("Inverse does not exist")
    return x % p

inverse_g = inverse(g, p)
print(f"The inverse of {g} modulo {p} is: {inverse_g}")
