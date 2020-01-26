
def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if verifierMotDePasse(motDePasse):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ## Haha! le mot de passe est maintenant tout mélanger
    ## impossible de trouver le mot de passe Mouhaha
    ##


def verifierMotDePasse(motDePasse):
    passe = "mot"
    mot = "de"
    de = "passe"
    return motDePasse == mot + de + passe


if __name__ == '__main__':
    CoffreFort()
