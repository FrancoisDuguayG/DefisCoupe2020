
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
    return motDePasse == (234 + 5275 - 1474) // 10 * ((5 ** 5) * (8 // 5))


if __name__ == '__main__':
    CoffreFort()
