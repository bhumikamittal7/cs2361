p = 17
g = 2

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
def group_elements(p):
    G = []
    for i in range(1,p+1):
        if gcd(i,p) == 1:
            G.append(i)
    return G

def group_generated_by_g(g,p):
    G = []
    for i in range(1,p+1):
        if gcd(i,p) == 1:
            G.append((g**i)%p)
    return G

print(group_elements(p))
print(group_generated_by_g(g,p))

#===============================================================================
#G = [2, 4, 8, 16, 15, 13, 9, 1]
# Input: $((G= G = \mathbb{Z}^*_17, q = 8, p = 17), g=2, h = 4)$ \\
# Output: $\alpha = 2$
#2^2 = 4 mod 17

# h = 4
# g = 2
# \alpha = 2
# p = 17
