
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
    return mot_de_passe == ("abcdefghijklmnopqrstwxyz"[5:20])[0:6]


if __name__ == '__main__':
    CoffreFort()
