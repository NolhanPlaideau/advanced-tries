class Panier():
    def __init__(self):
        """initialise la file comme une file vide."""

    def est_vide(self):
        """Renvoie True si file vide, False sinon"""

    def enfiler(self, e):
        """Ajoute l'élément e en dernière position de la file, ne renvoie rien."""

    def defiler(self):
        """retire le premier élément de la file et le renvoie"""


def remplir(self, panier_temp):
    while not panier_temp.est_vide():
        article = panier_temp.defiler()
        self.enfiler(article)

#------------------------------------------------Q1
Panier.enfiler((31002, "Café noir", 1.50, 50525))


#------------------------------------------------Q2
def remplir(self, panier_temp):
    while not panier_temp.est_vide():
        article = panier_temp.defiler()
        self.enfiler(article)


#------------------------------------------------Q3
def prix_total(self):
    total = 0
    temp = Panier()
    while not self.est_vide():
        article = self.defiler(temp)
        total += article[2]
        temp.enfiler(article)
    while not temp.est_vide():
        self.enfiler(temp.defiler())
    return total

#------------------------------------------------Q4
def Dure_course(self):
    Duree = 0
    temp = Panier()
    if Panier.est_vide(self) == True:
        return 0
    else:
        art1 = self.defiler(temp)
        while not temp.est_vide():
            artD = self.defiler()
    Duree = art1[3] - artD[3]
    return Duree