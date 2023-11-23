# Définition des fonctions pour les calculs de la calculatrice

# Fonction d'addition

def add(x, y):
    return x + y

# Fonction de soustraction
def subtract(x, y):
    return x - y

# Fonction de multiplication
def multiply(x, y):
    return x * y

# Fonction de division
def divide(x, y):
    if y == 0:
        return "Division par zéro"
    return x / y

# Menu pour choisir l'opération
def calc_menu():
    print("Calculatrice")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Choisissez une opération (1/2/3/4) : ")
    return choice

# Fonction qui execute tout le programe
def calc():
    while True:
        choice = calc_menu()
        
        if choice not in ['1', '2', '3', '4']:
            print("Choix invalide. Veuillez choisir une option valide.")
            continue
        
        x = float(input("Entrez le premier nombre : "))
        y = float(input("Entrez le deuxième nombre : "))

        if choice == '1':
            result = add(x, y)
            print(f"Résultat : {x} + {y} = {result}")
        elif choice == '2':
            result = subtract(x, y)
            print(f"Résultat : {x} - {y} = {result}")
        elif choice == '3':
            result = multiply(x, y)
            print(f"Résultat : {x} * {y} = {result}")
        elif choice == '4':
            result = divide(x, y)
            print(f"Résultat : {x} / {y} = {result}")

        another_calculation = input("Voulez-vous effectuer une autre opération ? (O/N) : ").strip().lower()
        if another_calculation != 'o':
            break

# Fonction de test pour les opérations de calcul
def test_calculator_operations():
    assert add(5, 3) == 8
    assert subtract(10, 4) == 6
    assert multiply(7, 2) == 14
    assert divide(8, 2) == 4
    assert divide(6, 0) == "Division par zéro"

# pour tester le module
if __name__ == "__main__":
    # unit tests - no output means all tests passed
    test_calculator_operations()

    # interface test - try to crash it
    calc()