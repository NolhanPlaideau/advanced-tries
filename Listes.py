from collections import deque
from random import randint

#----------------------------------------------------------------------------------
class Tru:
    def __init__(self):
        # Mise en place Valeur
        self.current = deque(maxlen=1)
        self.back = deque(maxlen=3)
        self.forback = deque(maxlen=3)

        self.back.append(1)
        self.back.append(2)

        self.current.append(4)

        self.forback.append("3")

        self.list = ""


    def __repr__(self):
        return(
            f" Back list :  {self.back}\n"
            f" Current list :  {self.current}\n"
            f" Forback list :  {self.forback}"
            )

# ---------------------------------------------------------------------------------- Defiler
    def defiler(self):
        list = input(
            'Which list do you want to dequeue ? : '
        ).lower()

        assert list in ("back", "current", "forback"), \
            "Enter a valid name: (back, current, forback)"

        if list == "back":
            self.list = self.back


        elif list == "current":
            self.list = self.current

        elif list == "forback":
            self.list = self.forback

        valeur = self.list.popleft()


        return (
            f"Valeur retirée : {valeur}\n"
            f"Back list : {self.back}\n"
            f"Current list : {self.current}\n"
            f"Forback list : {self.forback}"
        )

# ---------------------------------------------------------------------------------- Enfiler
    def enfiler(self):
        list = input ('Which list do you want to enqueue ? : ').lower()
        assert list in ("back", "current", "forback"), "Enter a valid name: (back, current, forback)"

        r = randint(1, 10)
        print(f"Voici la valeur : {r}")

        # Affiliation list
        if list == "back":
            self.list = self.back
            suivante = self.current

        elif list == "current":
            self.list = self.current
            suivante = self.forback

        elif list == "forback":
            self.list = self.forback
            suivante = None

        # Si file pleine
        if len(self.list) == self.list.maxlen:

            valeur = self.list.popleft()

            # Faire passer l'ancienne valeur dans la file suivante
            if suivante is not None:
                if len(suivante) == suivante.maxlen:
                    suivante.popleft()

                suivante.append(valeur)

        self.list.append(r)

        return (
            f" Back list :  {self.back}\n"
            f" Current list :  {self.current}\n"
            f" Forback list :  {self.forback}"
        )

#----------------------------------------------------------------------------------

def dmd ():
    resp = input(f"... \n\n"
        f"What do you want to do ? : ").lower()

    assert resp in ("defiler", "enfiler"), "Enter a valid name: (defiler, enfiler)"

    if resp == "defiler":
        print("\nAprès defiler :")
        print(test.defiler())

    elif resp == "enfiler" :
        print("\nAprès enfiler :")
        print(test.enfiler())

def co():
    dmd()
    while True:
        resp = input(
            f"... \n\n"
            "Do you want to continue ? : ").lower()

        assert resp in ("yes", "no"), "Enter a valid name: (yes, no)"

        if resp == "yes":
            dmd()

        else:
            return False

test = Tru()
print(test)

co()
