N = int(input('Entrer un entier N'))

p=2
while (N>1):
    while (N%p==0):
        N=N//p
        print(p)
    p=p+1