"""
Définition des fonctions pour les calculs de la 
calculatrice
"""
# Addition
def add(x, y):
    return x + y

# Soustraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    if y == 0:
        return "Division par zéro"
    return x / y

# Calculatrice
def calc():
    while True:
        print("Calculatrice:")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")

        choice = input("Sélectionnez une option: ")

        if choice == '5':
            break

        if choice in ['1', '2', '3', '4']:
            x = float(input("Entrez le premier nombre: "))
            y = float(input("Entrez le deuxième nombre: "))

            if choice == '1':
                result = add(x, y)
            elif choice == '2':
                result = subtract(x, y)
            elif choice == '3':
                result = multiply(x, y)
            elif choice == '4':
                result = divide(x, y)

            print("Résultat :", result)
        else:
            print("Option invalide")

calc()

# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":  
    # TODO ajouter des tests pour les fonctions
    calc()
