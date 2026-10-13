class aliment :
    def __init__(self, nom, energie, lipide, glucide, fibre, proteine, sel):
        self.nom = nom
        self.energie = energie
        self.lipide = lipide
        self.glucide = glucide
        self.fibre = fibre
        self.proteine = proteine
        self.sel = sel

#_________________________________________Question 2
    def __repr__(self):
        return(f'Intitulé: {self.nom}\n'
            f'Énergie: {self.energie}\n'
            f'Lipide : {self.lipide}\n'
            f'Glucide : {self.glucide}\n'
            f'Fibre  : {self.fibre}\n'
            f'Protéine : {self.proteine}\n'
            f'Sel: {self.sel}\n')

#__________________________________________Question 1
riz_blanc = aliment("riz blanc", 1532, 0.6, 81, 1.3, 7.2, 0.01)
print(riz_blanc)


#___________________________________________Question 2
print(100*riz_blanc.glucide)

#___________________________________________Question 4
salade_de_riz = [("riz", 500), ("thon", 200), ("tomate", 200),("oeuf_dur", 110), ("mais", 300)]

#________________a.
def mass_plat(plat):
    masse_plat = 0
    for item in plat:
        masse_plat = masse_plat + item[1]
    return masse_plat


print(f'masse_plat: {mass_plat(salade_de_riz)}')

#_______________b.
def energie_plat(plat):
    print(100*plat.energie)

#_______________c.
def fiche_info_nutrition(plat) :
    fiche_info_nutrition = {}
    for item in plat:
        fiche_info_nutrition[item[0]] = item[1]

    return fiche_info_nutrition