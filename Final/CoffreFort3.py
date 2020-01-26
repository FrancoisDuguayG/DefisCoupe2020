
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
    trois = 3
    quatre = "4"
    cinq = 5
    return motDePasse == trois * 3 + int(quatre) * 4 + cinq * 10


if __name__ == '__main__':
    CoffreFort()
