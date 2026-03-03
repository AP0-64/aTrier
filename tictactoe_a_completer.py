#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# Le code est à lire entièrement et à compléter dans l'ordre des numéros      #
###############################################################################

from random import randint # import de la fonction randint dans l'espace global


##############################################################################
#                    (1)  Compléter la fonction init()                       #
##############################################################################
def init()->list:
    """
    renvoie un plateau vide = tableau = liste de trois sous-listes de trois 0
    """
    pass











def affiche_plateau(plateau: list)->None:
    """
    affiche le plateau en argument qui contient des 0, 1 et -1.
    -1 : numéro de l'ordi qui met des O
    1 : numéro du joueur qui  met des X
    0 : la case est vide, elle n'a pas été jouée
    """
    print("-------")
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == 0:
                print("| ", end='')
            elif plateau[i][j] == 1:
                print("|X", end='')
            else:
                print("|O", end='')
        print("|")
        print("-------")

##############################################################################
#           (2)  Compléter la fonction gagne(plateau, joueur)                #
#                les lignes correspondant                                    #
#                aux tests des 3 colonnes et de la 2ème diagonale            #
##############################################################################
def gagne(plateau: list, joueur: int)->bool:
    """
    prend en argument un plateau de jeu et un numéro de joueur
    renvoie un booléen indiquant si le joueur a gagné
    -1 : numéro de l'ordi
    1 : numéro du joueur
    """
    ####################################################################
    # On teste les trois lignes :                                      #
    ####################################################################
    for i in range(3):
        j = 0
        while j < 3 and plateau[i][j] == joueur:
            j += 1
        if j == 3: # Si on arrive là, le joueur a une ligne gagnante
            return True
    ####################################################################
    # On teste les trois colonnes : (à vous de compléter)              #
    ####################################################################
    pass






    ####################################################################
    # On teste la 1ère diagonale :                                     #
    # (du coin en haut à gauche au coin en bas à droite)               #
    ####################################################################
    i = 0
    while i < 3 and plateau[i][i] == joueur:
        i += 1
    if i == 3: # Si on arrive là, le joueur a la 1ère diagonale gagnante
        return True 
    ####################################################################
    # On teste la 2ème diagonale : (à vous de compléter)               #
    # (du coin en haut à droite au coin en bas à gauche)               #
    ####################################################################
    pass






##############################################################################
#           (6) Compléter la fonction coup_gagnant(plateau, l, c)            #
##############################################################################
def coup_gagnant(plateau: list, l: int, c: int)->bool:
    """
    renvoie True si la case (l, c) est libre et que le coup est gagnant pour l'ordi
    renvoie False sinon
    """
    pass









##############################################################################
#           (8) Compléter la fonction coup_force(plateau, l, c)              #
##############################################################################
def coup_force(plateau: list, l: int, c:int)->bool:
    """
    renvoie True si (l, c) est libre et forcé pour éviter la défaite de l'ordi
    renvoie False sinon
    """
    pass








##############################################################################
#           (3) Compléter la fonction coup_valide(plateau, l, c)             #
##############################################################################
def coup_valide(plateau: list, l: int, c:int)->bool:
    """
    renvoie True si le coup dans la case (l, c) est possible
    c-à-d si les indices l et c sont valides et que la case correspondante est libre
    renvoie False sinon
    """
    pass



# Initialisation des variables :
plateau = init()
affiche_plateau(plateau)
partie_finie = False
qui_commence = int(input("Qui commence ?\nTaper 1 pour le joueur ou -1 pour l'ordi : "))
nb_coups = 0

# Si l'ordi commence
if qui_commence == -1:
    plateau[randint(0, 2)][randint(0, 2)] = -1
    nb_coups += 1
    print("Voici mon coup :")
    affiche_plateau(plateau)

# Que l'ordi est commencé ou pas, c'est au joueur de jouer

while partie_finie == False:

    # Vérification de la validité du coup
    coup_effectue = False
    while coup_effectue == False:
        ligne = int(input("Choisir une ligne (entre 1 et 3) : ")) - 1
        colonne = int(input("Choisir une colonne (entre 1 et 3) : ")) - 1
        if not coup_valide(plateau, ligne, colonne):
            print("La case est occupée ou les indices ne sont pas entre 1 et 3, rejouez !")
        else:
            plateau[ligne][colonne] = 1
            coup_effectue = True
            affiche_plateau(plateau)
            nb_coups += 1
    
    if gagne(plateau, 1): # Fin de partie
        print("Bravo !")
        partie_finie = True
        
    elif nb_coups == 9:
        print("Match nul !")
        partie_finie = True
        
    else:  # La partie continue et c'est à l'ordi de jouer
        coup_effectue = False

        ###############################################################
        #             (7) Compléter les lignes ci-dessous             #
        ###############################################################
        # Recherche d'un coup gagnant et le jouer s'il existe
        pass






   
        ###############################################################
        #             (9) Compléter les lignes ci-dessous             #
        ###############################################################
        # Recherche d'un coup forcé et le jouer s'il existe
        pass







    
        ###############################################################
        #             (4) Compléter les lignes ci-dessous             #
        ###############################################################
        # Un coup aléatoire est joué par l'ordi
        # Tant que le coup n'est pas joué,
        # on choisit au hasard une ligne et une colonne
        # l'ordi joue ce coup si la case est libre (on y place -1 à la place du 0)
        # puis on incrémente nb_coups et on affecte True à coup_effectue
        while coup_effectue == False:
            pass
            pass
            if plateau[ligne][colonne] == 0:
                pass


                print()
                print("Voici mon coup :")
                affiche_plateau(plateau)
                
        ###############################################################
        #             (5) Compléter les lignes ci-dessous             #
        ###############################################################
        # Fin de partie : victoire de l'ordi ou nul
        # Si l'ordi a gagné, on affiche "Perdu !" et on affecte True à partie_finie
        # Sinon si nb_coups vaut 9, on affiche "Match nul !" et on affecte True à partie_finie
        pass
        
    







