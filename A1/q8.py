n = 793872007422642643069
a = 3478293847392
b = 70934603673

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

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

gcd_a = gcd(a, n)
print(f"The gcd of {a} and {n} is: {gcd_a}")

gcd_b = gcd(b, n)
print(f"The gcd of {b} and {n} is: {gcd_b}")

if gcd_a == 1:
    inverse_a = inverse(a, n)
    print(f"The inverse of {a} modulo {n} is: {inverse_a}")

if gcd_b == 1:
    inverse_b = inverse(b, n)
    print(f"The inverse of {b} modulo {n} is: {inverse_b}")