def volcan():
    with open('messagePourSauverLeMonde.txt', 'r') as file:
        for line in file:
            for word in line.split():
                print(word)
                if word == "volcan":
                    print("A l’aide, tous aux abris !")
    file.close()


def arbre():
    file = open("livreDeLaNatureEtDesLacs.txt")
    line = file.readline()
    while line:
        if "arbre" in line and "lac" in line:
            print(line)
        line = file.readline()


def repere():
    gauche = 0
    avant = 0
    droite = 0
    nbr_pas = 0
    lac = False
    while lac is False and nbr_pas < 100:
        with open('desProjectilesEtDesDodos.txt', 'r') as file:
            for line in file:
                for word in line.split():
                    if word == "rocher":
                        print("rocher")
                        gauche += 5
                        nbr_pas += 5
                    if word == "arbre":
                        print("arbre")
                        avant += 10
                        nbr_pas += 10
                    if word == "dodo":
                        print("dodo")
                        droite += 6
                        nbr_pas += 6
                    if word == "lac" and nbr_pas >= 100:
                        if gauche > avant and gauche > droite:
                            plus_de_pas = gauche
                            print("gauche")
                        elif avant > gauche and avant > droite:
                            plus_de_pas = avant
                            print("avant")
                        elif droite > gauche and droite > avant:
                            plus_de_pas = droite
                            print("droite")
                        return nbr_pas, "", plus_de_pas


def numero():
    liste = []
    with open('lafamilleDodo.txt', 'r') as file:
        for line in file:
            try:
                for number in line.split(", "):
                    number = int(number)
                    if number not in liste:
                        liste.append(number)
            except:
                continue

    with open('lafamilleDodo.txt', 'w') as file:
        liste.sort()
        for i in liste:
            file.write(str(i))
    return liste


def ages():
    nombre_majeurs = 0
    nombre_mineurs = 0
    with open('ageDodo.txt', 'r') as file:
        for line in file:
            for age in line.split(", "):
                if int(age) > 5:
                    nombre_majeurs += 1
                else:
                    nombre_mineurs += 1
    return f'il y a {nombre_majeurs} majeurs et {nombre_mineurs} mineurs'
