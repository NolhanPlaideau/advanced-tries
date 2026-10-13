#_____________________________________________ Arbres
class noeud :
    def __init__(self,racine):
        self.gauche= "ccoo"
        self.racine=racine
        self.droit=  "oco"
    def __repr__(self):
        return f'{self.racine}({str(self.gauche)},{str(self.droit)})'

window = noeud("coco")
print(window)

"""compte la hauteur d'un arbre"""
def hauteur (self) :
    if self == None :
        return -1
    else :
        hauteur_gauche = self.gauche.hauteur () if self.gauche else -1
        hauteur_droite = self.droit.hauteur () if self.droit else -1
    return 1 + max (hauteur_gauche , hauteur_droite)

"""Compte la taille d'un arbre"""
def taille (self) :
    if self == None :
        return 0
    else :
        taille_gauche = self.gauche.taille() if self.gauche else 0
        taille_droit = self.droit.taille () if self.droit else 0
    return 1 + taille_gauche + taille_droit
#__________________________________________________ listes successeurs
Transport = {"Paris" : [("Strasbourg", 490),("Brest", 592)],
            "Brest" : [("Paris", 592),("Nantes", 292)],
             "Nantes" : [("Brest", 295)],
             "Starbourg" : [("Paris", 490)],}

def est_dans (G, v):
    return v in G.keys()

def voisins (G, v):
    if est_dans(G, v):
        return [sommet for sommet, poids in G[v]]
    else:
        return []

#___________________________________________________ Matrice
graph_proba = [[0.1, 0.5, 0.4],
               [0, 0.35, 0.65],
               [0.8, 0, 0.2]]

#____________________________________________________ Passage d'une représentation à une autre
"""De la représentation matricielle à la représentation par listes successeurs"""
def matrice_vers_listes_succ(matrice):
    listes_succ = {i: [] for i in range(len(matrice))}   # Initialisation des listes de successeurs
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:  # S'il y a une arête de i vers j
                listes_succ[i].append(j)
    return listes_succ

""""De la représentation par listes successeurs à la représentation matricielle"""
def listes_succ_to_matrice(listes_succ):
    n = len(listes_succ)  # Nombre de sommets
    matrice = [[0] * n for _ in range(n)]  # Initialisation de la matrice
    for i in listes_succ:
        for j in listes_succ[i]:
            matrice[i][j] =  1 # Ajout des arêtes
    return matrice
