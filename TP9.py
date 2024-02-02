from math import floor

def binaire(n) :
    resu = ''
    while n > 0:
        a = n//2
        b = n % 2
        resu = str(b) + resu
        n = a
    return resu

def binaire_virgule(x) :
    n = floor(x)
    resu = binaire(n) + ","
    x = x - n
    while x > 0 :
        y = x * 2
        z = floor(y)
        x = y - z
        #print(z)
        resu = resu + str(z)
    return resu

print(binaire(75))
print(binaire_virgule(25.8125))
