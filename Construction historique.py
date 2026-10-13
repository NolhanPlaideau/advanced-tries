from collections import deque

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QMessageBox,
    QListWidget,
    QDialog,
    QVBoxLayout
)

# -------------------------------------------------------------------- Interface
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Construction historique")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(600, 450)

        # Widget central
        container = QWidget()
        self.setCentralWidget(container)

        # Layout principal
        layout = QHBoxLayout(container)

        # --------------------------------------------------------------------- listes

        self.back = deque()
        self.back.appendleft('a')
        self.back.appendleft('b')
        self.back.appendleft('c')

        self.current = deque()
        self.current.appendleft('1')

        self.forward = deque()
        self.forward.appendleft('d')
        self.forward.appendleft('e')
        self.forward.appendleft('f')

        print(self)

        # --------------------------------------------------------------------
        # Bouton

        button = QPushButton("Start")
        button.clicked.connect(self.start)

        layout.addWidget(button)

    # --------------------------------------------------------------------
    # Affichage de l'objet

    def __repr__(self):
        return (
            f"Back: {self.back}\n"
            f"Current: {self.current}\n"
            f"Forward: {self.forward}"
        )

    # --------------------------------------------------------------------
    # Choix de l'onglet

    def choice(self):

        Onglet = QDialog(self)
        Onglet.setWindowTitle("Onglet")

        layout = QVBoxLayout(Onglet)

        listWidget = QListWidget()

        listWidget.addItems([
            "Onglet1",
            "Onglet2",
            "Onglet3"
        ])

        layout.addWidget(listWidget)

        # Attend que l'utilisateur sélectionne un élément
        listWidget.itemClicked.connect(Onglet.accept)

        Onglet.exec()

        item = listWidget.currentItem()

        if item is None:
            return None

        if item.text() == "Onglet1":
            return "O1"

        elif item.text() == "Onglet2":
            return "O2"

        elif item.text() == "Onglet3":
            return "O3"

    # --------------------------------------------------------------------
    # Question Avancer / Reculer

    def instruction_base(self, reponse):

        message = QMessageBox(self)

        message.setWindowTitle("Question")
        message.setText(
            f"Onglet sélectionné : {reponse}\n\n"
            "Quelle action voulez-vous exécuter ?"
        )

        avancer = message.addButton(
            "Avancer",
            QMessageBox.ButtonRole.AcceptRole
        )

        reculer = message.addButton(
            "Reculer",
            QMessageBox.ButtonRole.RejectRole
        )

        message.exec()

        # ---------------------------------------------------------------
        # AVANCER

        if message.clickedButton() == avancer:

            # Vérifie qu'il existe une page dans forward
            if len(self.forward) == 0:
                QMessageBox.information(
                    self,
                    "Impossible",
                    "Il n'y a aucune page suivante."
                )
                return

            self.back.appendleft(self.current.popleft())

            self.current.appendleft(self.forward.popleft())

        # ---------------------------------------------------------------
        # RECULER

        elif message.clickedButton() == reculer:

            # Vérifie qu'il existe une page dans back
            if len(self.back) == 0:
                QMessageBox.information(
                    self,
                    "Impossible",
                    "Il n'y a aucune page précédente."
                )
                return

            self.forward.appendleft(
                self.current.popleft()
            )

            self.current.appendleft(
                self.back.popleft()
            )

        # Affiche le résultat après le déplacement
        self.afficher_resultat()

    # --------------------------------------------------------------------
    # Fonction Start

    def start(self):

        reponse = self.choice()

        if reponse is None:
            return

        self.instruction_base(reponse)

    # --------------------------------------------------------------------
    # Afficher le résultat

    def afficher_resultat(self):

        result = QMessageBox(self)

        result.setWindowTitle("Result")

        result.setText(
            f"Back: {self.back}\n"
            f"Current: {self.current}\n"
            f"Forward: {self.forward}"
        )

        result.exec()




# --------------------------------------------------------------------

app = QApplication([])

window = MainWindow()
window.show()

app.exec()