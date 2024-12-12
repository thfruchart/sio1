# TP :  CARRE MAGIQUE

carre = [[1,2,3],
         [4,5,6],
         [7,8,9]]

rectangle = [[1,4,6,7],
             [8,5,3,2]]

carremagique = [[8,1,6],
                [3,5,7],
                [4,9,2]]

grandcarre = [[12,6,15,1],
              [13,3,10,8],
              [2,16,5,11],
              [7,9,4,14]]


def mystere(tab):
    test = True
    for i in range(1,len(tab)):
        if tab[i] != tab[0]:
            test = False
    return test



def total_par_ligne(tab):
    n = len(tab)
    m = len (tab[0])
    resu = [0 for i in range(n)]
    for i in range(n):
        for j in range(m):
            resu[i] = resu[i] + tab[i][j]
    return resu

def total_par_colonne(tab):
    n = len(tab)
    m = len (tab[0])
    resu = [0 for i in range(m)]
    for i in range(n):
        for j in range(m):
            resu[j] = resu[j] + tab[i][j]
    return resu

def magique(tab):
    lig = total_par_ligne(  tab )
    col = total_par_colonne(  tab )
    print(mystere(lig))
    print(mystere(col))
    if mystere(lig) and mystere(col) :
        resu =  True
    else :
        resu =  False
    return resu

def magique(tab):
    return mystere(total_par_ligne( tab )) and mystere(total_par_colonne( tab ))

print('magique(carre) : ' , magique(carre))
print('magique(carre) : ' , magique(carremagique))
print('magique(rectangle) : ' , magique(rectangle))
print('magique(grandcarre) : ' , magique(grandcarre))
