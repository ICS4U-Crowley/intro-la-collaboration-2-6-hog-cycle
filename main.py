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

        if choice == "calc":
            calc.calc()
        elif choice == "animate":
            anim.animate()
        elif choice ==  "exit":
            break
        else:
            print("Invalid, Essayer Encore!.")
        
        cli.clear()
    

def terminate():
    """() -> None"""
    cli.close()


if __name__ == "__main__":
    # Logique globale du programme (menu infini avec option de sortie)
    initialise()
    loop()
    terminate()