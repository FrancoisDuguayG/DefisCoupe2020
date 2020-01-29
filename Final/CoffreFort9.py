
def CoffreFort():
    mot_de_passe = 0
    try:
        mot_de_passe = int(input("Entrez votre mot de passe: "))
    except ValueError:
        print("ERREUR!#?!")
    if verifier_mot_de_passe(int(mot_de_passe)):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ##
    ##
    ##


def verifier_mot_de_passe(mot_de_passe):
    liste_de_chiffres = [31, 25, 19, 13, 7, 1]

    crypto_mp = 0

    for chiffre in liste_de_chiffres:
        crypto_mp += liste_de_chiffres[chiffre % 5]

    print(crypto_mp)
    return mot_de_passe == crypto_mp


if __name__ == '__main__':
    CoffreFort()
