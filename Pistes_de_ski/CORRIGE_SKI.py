# CORRECTION

pistes=[['A','B','B','C','C','D','D','E','F'],
        ['B','C','E','A','D','A','E','F','D']]

parcours1='BEF'
parcours2='ABCDFDA'
parcours3='DABEFDA'


def piste_ouverte(debut, fin):
    valide=False
    for i in range(9):
        if pistes[0][i]==debut and pistes[1][i]==fin:
            valide=True
    return valide

def parcours_valide(parcours):
    for i in range(len(parcours) - 1):
        deb = parcours[i]
        fin = parcours[i+1]
        test = piste_ouverte(deb,fin)

        if test == False :
            print(deb, fin, "n'est pas une piste ouverte")
            return False
    return True

parc = input("Saisir un parcours : ")
print(parcours_valide(parc))
