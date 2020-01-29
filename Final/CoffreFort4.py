
def CoffreFort():
    mot_de_passe = 0
    try:
        mot_de_passe = int(input("Entrez votre mot de passe: "))
    except ValueError:
        print("ERREUR!#?!")
    if verifier_mot_de_passe(mot_de_passe):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ##
    ##
    ##


def verifier_mot_de_passe(mot_de_passe):
    return mot_de_passe == (234 + 5275 - 1474) // 10 * ((5 ** 2) * (8 // 5))


if __name__ == '__main__':
    CoffreFort()
