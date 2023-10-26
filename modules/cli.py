import os

"""
Définitions des méthodes pour l'interface de ligne de commande,
l'interface utilisateur à la console
"""

def greet():
    """() -> None"""
    
    print("Bien veneu a ce programme tu peut reagarder un animation dun cube puis tu peut faire des calcul")

def menu(items):
    """(list:str) -> str
    Retourne le nombre de la position de l'item dans la liste des items.
    Le 1e item retourne la valeur 1, etc. Aucune validation des valeurs invalides.
    """
    
    for i in items:
        print(items.index(i)+1, i)
    return input ("saisir votre choix (metter un des trois numero): ")

def clear():
    """() -> None"""
    os.system('cls' if os.name == 'nt' else 'clear')

def close():
    """() -> None"""
   
    print("Merci pour utiliser notre programme a la prochain.")

# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":  
    
    clear()
    greet()
    choix = menu(["option 1", "option 2", "option 3"])
    print("choix =", choix)
    close()
    menuCalc()