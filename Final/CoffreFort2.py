
def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if verifierMotDePasse(motDePasse):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ## Pour réussir à briser cette serrure il
    ## faudrait être capable de multiplier des lettres Mouhaha!
    ## Même si ça ressemble beaucoup à l'addition de lettre


def verifierMotDePasse(motDePasse):
    trois = 3
    quatre = "4"
    return motDePasse == str(trois * 4) + quatre * 3


if __name__ == '__main__':
    CoffreFort()
