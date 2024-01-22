def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Division par zéro impossible")

def calculatrice():
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        operateur = input("Entrez l'opérateur (+, -, *, /) : ")
        nombre2 = float(input("Entrez le deuxième nombre : "))

        if operateur == '+':
            resultat = addition(nombre1, nombre2)
        elif operateur == '-':
            resultat = soustraction(nombre1, nombre2)
        elif operateur == '*':
            resultat = multiplication(nombre1, nombre2)
        elif operateur == '/':
            resultat = division(nombre1, nombre2)
        else:
            raise ValueError("Opérateur invalide")

        print(f"Le résultat de {nombre1} {operateur} {nombre2} est : {resultat}")

    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


calculatrice()
