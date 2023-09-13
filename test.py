def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
p = 16868678779879798798798797465465479

#given a generator g, find the inverse of g
g = 53

def inverse(g,p):
    for i in range(1,p):
        if (g*i)%p == 1:
            return i

print(inverse(g,p))