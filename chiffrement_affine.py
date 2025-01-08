ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def RANG(car) :
    resu = -1
    i = 0
    while (i<26) and (resu == -1) :
        if (car == ALPHABET[i]) :
            resu = i
        i = i+1
    return resu
