import hashlib
k = 245
T = 2**k
loop = 2**(256-k)
prefix = "bhumika.mittal_ug24@ashoka.edu.in"
for i in range(loop):
    h = hashlib.sha256()
    h.update((prefix+str(i)).encode())
    a = h.hexdigest()
    print(a)
    if(int(str(a), 16) < T):
        print(".....................")
        print("....a solution is found and the number of iterations it took:", i)
        print("Number of leading zeros:", 256-k)
        print(a)
        print("{0:0256b}".format(int(str(a), 16)))
        break


