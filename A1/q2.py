def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
p = 8
G = []
for i in range(1,p+1):
    if gcd(i,p) == 1:
        G.append(i)
print(G)

i = 4
if i in G:
    for j in range(1,p+1):
        if((i**j)%p == 1):
            print("order of",i,"is",j)
            break
