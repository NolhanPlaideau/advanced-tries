from collections import deque

class Panier:
    def __init__(self):
        self.panier = deque()

    def est_vide(self):
        if len(self.panier) == 0:
            return True
        else:
            return False

    def enfiler(self):
        code_barre = input("Veuillez entrer le code-barres de votre article : ")
        designation = input("Veuillez entrer la désignation de votre article : ")
        prix = input("Veuillez entrer le prix de votre article : ")
        horaire_scan = input("Veuillez entrer l'horaire de l'achat de votre article : ")

        e = [code_barre, designation, prix, horaire_scan]
        self.panier.append(e)

    def defiler(self):
        if not self.est_vide():
            self.panier.popleft()
        else:
            print("Le panier est vide.")

    def afficher(self):
        print(self.panier)


print("Quelle action voulez-vous exécuter ?")
print("Print (P), Empty or not (E), Add (A), Withdraw (W)")

W = input().upper()

assert W in ("P", "E", "A", "W"), "Entrez une valeur correcte :"

window = Panier()

if W == "P":
    window.afficher()

elif W == "E":
    print(window.est_vide())

elif W == "A":
    window.enfiler()

elif W == "W":
    window.defiler()