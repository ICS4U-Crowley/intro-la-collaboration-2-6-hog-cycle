# Fonction d'addition
def addition():
    x = float(input("Entrez le premier nombre : "))
    y = float(input("Entrez le deuxième nombre : "))
    return x + y

# Fonction de soustraction
def soustraction():
    x = float(input("Entrez le premier nombre : "))
    y = float(input("Entrez le deuxième nombre : "))
    return x - y

# Fonction de multiplication
def multiplication():
    x = float(input("Entrez le premier nombre : "))
    y = float(input("Entrez le deuxième nombre : "))
    return x * y

# Fonction de division
def division():
    x = float(input("Entrez le numérateur : "))
    y = float(input("Entrez le dénominateur : "))
    if y == 0:
        return "Division par zéro"
    return x / y

# Code pour tester ce module indépendamment du programme principal
if __name__ == "__main__":
    # Tests unitaires pour les fonctions
    resultat = addition()
    print(f"Addition : Résultat = {resultat}")

    resultat = soustraction()
    print(f"Soustraction : Résultat = {resultat}")

    resultat = multiplication()
    print(f"Multiplication : Résultat = {resultat}")

    resultat = division()
    print(f"Division : Résultat = {resultat}")
