import os

"""
Définitions des méthodes pour l'interface de ligne de commande,
l'interface utilisateur à la console
"""

def greet():
    """() -> None"""
    # TODO afficher un message d'acceuil
    print("Insérer un message d'accueil ici")

def menu(items):
    """(list:str) -> str"""
    # TODO remplacer les instructions ci-dessous pour \
    # afficher correctement les instructions, le menu et \
    # pour saisir le choix
    for i in items:
        print(i)
    return ""

def clear():
    """() -> None"""
    os.system('cls' if os.name == 'nt' else 'clear')

def close():
    """() -> None"""
    # TODO afficher un message de sortie
    print("Insérer un message de sortie ici")

# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":  
    # TODO ajouter/modifier les tests unitaires pour les fonctions
    clear()
    greet()
    choix = menu(["un", "deux", "trois"])
    print("choix =", choix)
    close()
    