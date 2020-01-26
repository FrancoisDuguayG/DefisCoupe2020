
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
    if len(motDePasse) != 14:
        return False

    motDePasseEncrypte = ""

    for i in range(0, 6):
        motDePasseEncrypte += motDePasse[i]

    for i in range(13, 5, -1):
        motDePasseEncrypte += motDePasse[i]

    return motDePasseEncrypte == "vive_l!epuoc_a"



if __name__ == '__main__':
    CoffreFort()
