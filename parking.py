# CCF Parking

lane = [ 0,1,0,0,0,1,0,1]

parking = [ [0,0,0,0,0,0,0,0],
            [0,1,0,0,0,1,0,0],
            [0,1,1,0,0,1,1,1],
            [1,1,1,1,1,1,1,1]]

def occup(tab):
    i = 0
    test = False
    while i < 8:
        val = tab[i]
        if val == 1 :
            test =  True
        i = i+1
    return test




def mystere(tab):
    resu = 0
    for i in range(8):
        val = tab[i]
        resu = resu + val
    return resu

def places_dispo(tab):
    places = [0,0,0,0]
    for i in range(4):
        etage = tab[i]
        print(etage, mystere(etage))

    return places
