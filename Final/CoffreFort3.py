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
    trois = 3
    quatre = "4"
    cinq = 5
    return mot_de_passe == trois * 3 + int(quatre * 2) + cinq * 10


if __name__ == '__main__':
    CoffreFort()
