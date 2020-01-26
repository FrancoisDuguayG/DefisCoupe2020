
def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if verifierMotDePasse(motDePasse):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ##
    ##
    ##


def verifierMotDePasse(motDePasse):
    return motDePasse == ("abcdefghijklmnopqrstwxyz"[5:20])[0:6]


if __name__ == '__main__':
    CoffreFort()
