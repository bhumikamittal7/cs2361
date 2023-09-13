def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
p = 13
G = []
for i in range(1,p+1):
    if gcd(i,p) == 1:
        G.append(i)
# print(G)

g = [] #list of generators
for i in G:
    for j in range(1,p+1):
        if((i**j)%p == 1):
            if(j == p-1):
                g.append(i)
            break
print(g)