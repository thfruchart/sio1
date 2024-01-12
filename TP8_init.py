# TP8

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 5
b = 17

def RANG(car):
    resu = -1
    i = 0
    while (i<26) and resu == -1:
        if (car ==ALPHABET[i]):
            resu = i
        # if_end
        i = i+1
    #for_end
    return resu