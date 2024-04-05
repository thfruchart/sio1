# CCF Parking

lane = [ 0,1,0,0,0,1,0,1]

parking = [ [0,0,0,0,0,0,0,0],
            [0,1,0,0,0,1,0,0],
            [0,1,1,0,0,1,1,1],
            [1,1,1,1,1,1,1,1]]

def occup(tab):
    i = 0
    while i < 8:
        val = tab[i]
        if val == 1 :
            return True
        i = i+1
    return False

def mystere(tab):
    resu = 0
    for i in range(8):
        val = tab[i]
        resu = resu + val
    return resu

def places_dispo(tab):
    places = [0,0,0,0]
    for i in range(4):
        rangee = tab[i]
        places_libres = mystere(rangee)
        places[i] = places_libres
    return places