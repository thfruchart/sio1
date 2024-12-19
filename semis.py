# semis-console-init.py

NB_CASES = 6
plateau = [2]*NB_CASES
# la variable joueur alterne entre +1 et -1
joueur = +1


def tour_de_jeu(plateau, joueur, i):
    """modifie le plateau en faisant jouer la case d'indice i  au joueur (+1 ou -1)
    renvoie True si le coup est possible
    et False si le coup est perdant"""

    print("état initial du plateau :", plateau)
    print('joueur',joueur)
    print("case n°",i)
    nb_grains = ...
    dernier_indice = ...

    return


# test1 : dépassement
plateau1 = [1,2,3,0,2,2]
tour_de_jeu(plateau1, +1, 4)
print(plateau1)
print()


# test2 : dernière case vide
plateau2 = [3,2,1,0,2,2]
tour_de_jeu(plateau1, +1, 1)
print(plateau2)
print()

# test3 : coup valide pour le joueur 1
plateau3 = [1,2,3,0,2,2]
tour_de_jeu(plateau1, +1, 0)
print(plateau3)
print()


# test4 : coup valide pour le joueur -1
plateau4 = [1,2,3,0,2,2]
tour_de_jeu(plateau1, -1, 4)
print(plateau4)
print()
