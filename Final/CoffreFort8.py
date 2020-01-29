
def CoffreFort():
    mot_de_passe = input("Entrez votre mot de passe: ")
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

    for i in range(0, 6):
        crypto_mp += mot_de_passe[i]

    for i in range(13, 5, -1):
        crypto_mp += mot_de_passe[i]

    return crypto_mp == "v1v3_l!3pu0c_4"



if __name__ == '__main__':
    CoffreFort()
