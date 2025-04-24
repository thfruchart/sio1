Labyrinthe=[['X','X',' ','X','X','X',' ','X','X','X'],
	    ['X',' ',' ',' ','X',' ',' ',' ',' ','X'],
            ['X','X','X',' ','X','X','X','X',' ','X'],
            ['X',' ',' ',' ',' ',' ','X',' ',' ','X'],
            ['X','X',' ','X','X',' ',' ',' ','X','X'],
            [' ',' ',' ','X',' ','0','X','X',' ',' '],
            ['X',' ','X',' ','X',' ','X','X',' ','X'],
            ['X',' ',' ',' ',' ',' ','X','X',' ','X'],
            ['X',' ','X',' ','X',' ',' ',' ',' ','X'],
            ['X','X','X','X','X','X','X','X','X','X']]


def affichage():
    for i in range (10):
        print(Labyrinthe[i])



def teste_cases_adjacentes(i,j,n):
    #teste les cases adjacentes à   L[i][j]#
    #n est un entier qui represente la longueur des chemins deja  cherches#
    #si une case adjacente à  L[i][j] contient un espace, on ecrit 'n+1' à  la place#
    #on commence par tester si on ne sort pas du labyrinthe en se decalant d'une case#
    if (i-1>=0):
        if Labyrinthe[i-1][j]==' ':
            Labyrinthe[i-1][j]=str(n+1)
    if (j-1>=0):
        if Labyrinthe[i][j-1]==' ':
            Labyrinthe[i][j-1]=str(n+1)
    if (i+1<10):
        if Labyrinthe[i+1][j]==' ':
            Labyrinthe[i+1][j]=str(n+1)
    if (j+1<10):
        if Labyrinthe[i][j+1]==' ':
            Labyrinthe[i][j+1]=str(n+1)


def parcourir_lab(n):
    for i in range(10):
        for j in range(10):
            if Labyrinthe[i][j]==str(n):
                teste_cases_adjacentes(i,j,n)



def nombre_cases_vides(Labyrinthe):
    compteur=0
    for i in range(len(Labyrinthe)):
        for j in range(len(Labyrinthe[0])):
            if Labyrinthe[i][j]==' ':
                compteur=compteur+1
            #IfEnd
        #ForEnd
    #ForEnd
    return compteur

affichage()
print(' - - - ')
parcourir_lab(0)
affichage()
print(' + + + ')
parcourir_lab(1)
affichage()

