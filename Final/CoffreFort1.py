
def CoffreFort():
    mot_de_passe = input("Entrez votre mot de passe: ")
    if verifier_mot_de_passe(mot_de_passe):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ## Haha! le mot de passe est maintenant tout mélanger
    ## impossible de trouver le mot de passe Mouhaha
    ##


def verifier_mot_de_passe(mot_de_passe):
    passe = "mot"
    mot = "de"
    de = "passe"
    return mot_de_passe == mot + de + passe


if __name__ == '__main__':
    CoffreFort()
