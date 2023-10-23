import modules.calculations as calc
import modules.cli as cli
import modules.animations as anim

"""
Point de lancement du programme
"""

options = ["Calculatrice", "Animation", "Quitter"]

def initialise():
    """() -> None"""
    cli.clear()
    cli.greet()

def loop():
    """() -> None"""
    while (True):
        choice = cli.menu(options)

        # TODO supprimer les appels bidons ci-dessous en \
        # les insérant dans une structure logique appropriée \
        # pour la gestion du choix
        calc.calc()
        anim.animate()
        
        cli.clear()

        # TODO briser la boucle de façon appropriée dans la structure logique
        return 

def terminate():
    """() -> None"""
    cli.close()


if __name__ == "__main__":
    # Logique globale du programme (menu infini avec option de sortie)
    initialise()
    loop()
    terminate()