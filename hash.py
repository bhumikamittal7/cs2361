m = "blah message for q5 of the PP which will be signed using my sk. also this course is fun and tough ://"
# parameters = (p,q,g) = (17,8,2)

from hashlib import sha1
def hash(m):
    return int(sha1(m.encode()).hexdigest(),16)

def find_a(p,q,g):
    for a in range(1,q):
        if (g**a)%p == 1:
            return a
        
def generate_keys(p,q,g):
    a = find_a(p,q,g)
    h = (g**a)%p
    return (h,a)

def pk(h,p,q,g):
    return (h,p,q,g)

def sk(a,p,q,g):
    return a

def sign(m, k, a, p, q, g):
    z = hash(m)
    r = (g**k)%p%q
    c1 = (g**r))%p%q
    if(c1 != 0):
        c2 = (z + a*r)%q
        if (c2 != 0):
            return (c1,c2)
        else:
            return "Error: c2 = 0"
    else:
        return "Error: c1 = 0"

def verify(m, sig, h, p, q, g):
    z = hash(m)
    c1 = sig[0]
    c2 = sig[1]
    v1 = (g**z)%p%q
    v2 = (h**c1)%p%q
    v3 = (v1*v2)%p%q
    if (v3 == c1):
        return True
    else:
        return False
    

print(find_a(17,8,2))
        
