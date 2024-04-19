# AUTOMATE CELLULAIRE

etap=[[0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,1,0,1,0],
      [0,0,0,0,0,1,1,0],
      [0,0,0,0,1,0,1,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0]]


def compt_voisine(tab,i,j):    #  RENVOIE LE NOMBRE DE CASES VOISINES VIVANTES DE LA CASE LIGNE i ET COLONNE j DU TABLEAU tab
   compt=0
   if i>0:
        compt=compt+tab[i-1][j]
        if j>0:
            compt=compt+tab[i-1][j-1]
        if j<7:
            compt=compt+tab[i-1][j+1]
   if i<7:
        compt=compt+tab[i+1][j]
        if j>0:
            compt=compt+tab[i+1][j-1]
        if j<7:
            compt=compt+tab[i+1][j+1]
   if j>0:
        compt=compt+tab[i][j-1]
   if j<7:
        compt=compt+tab[i][j+1]
   return compt

def etap_compt(tab):        #  RENVOIE UN TABLEAU DE MEMES DIMENSIONS QUE LE TABLEAU tab ET CONTENANT POUR CHAQUE CASE LE NOMBRE DE CASES VIVANTES QUI L ENTOURENT
    global etap
    etap_compt=[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]
    for i in range(8):
        for j in range(8):
            etap_compt[i][j]=compt_voisine(etap,i,j)
    return etap_compt




tab_compt = etap_compt(etap)
# parcours des deux tableaux
for i in range(len(etap)):
    for j in range(len(etap[0])):
        cellul = etap[i][j]
        nb_voisines = tab_compt[i][j]
        if cellul == 1 : #cellule VIVANTE
            # la cellule survit si elle possède 2 ou 3 voisines
            if nb_voisines == 2  or nb_voisines == 3 :
                etap[i][j] = 1
            else :
                etap[i][j] = 0 # une cellule vivante meurt à l'étape suivante
        else : # cellule morte
            # s'il y a exactement trois voisines vivantes => naissance
            if nb_voisines == 3:
                etap[i][j] = 1

