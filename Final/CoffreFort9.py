
def CoffreFort():
    mot_de_passe = 0
    try:
        mot_de_passe = input("Entrez votre mot de passe: ")
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
    if len(mot_de_passe) != 14:
        return False

    crypto_mp = ""

    for position in range(1, 15):
        crypto_mp = crypto_mp + mot_de_passe[-position]

    print(crypto_mp)
    return crypto_mp == "!3pu0c_4l_3v1v"


if __name__ == '__main__':
    CoffreFort()
