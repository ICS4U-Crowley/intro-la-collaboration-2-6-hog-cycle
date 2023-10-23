from turtle import *

def animate():
    print("Action d'animation")
    try:
        # TODO code d'animation turtle ici
        mainloop()
    except Terminator as e:
        print('...la fenêtre a été fermée')

# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":  
    # TODO ajouter des tests unitaires pour les fonctions
    animate()