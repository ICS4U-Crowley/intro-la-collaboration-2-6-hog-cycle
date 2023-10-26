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
        choix  = cli.menu(options)

        if choix == "calc":
            calc.calc()
        elif choix == "animate":
            anim.animate()
        elif choix ==  "exit":
            break
        else:
            print("Choix Invalid, Essayer Encore!.")
        
        cli.clear()
    

def terminate():
    """() -> None"""
    cli.close()


if __name__ == "__main__":
    # Logique globale du programme (menu infini avec option de sortie)
    initialise()
    loop()
    terminate()