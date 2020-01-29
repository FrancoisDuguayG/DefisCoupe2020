
def CoffreFort():
    mot_de_passe = input("Entrez votre mot de passe: ")
    if verifier_mot_de_passe(mot_de_passe):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ## Pour réussir à briser cette serrure il
    ## faudrait être capable de multiplier des lettres Mouhaha!
    ## Même si ça ressemble beaucoup à l'addition de lettre


def verifier_mot_de_passe(mot_de_passe):
    trois = 3
    quatre = "4"
    return mot_de_passe == str(trois * 4) + quatre * 3


if __name__ == '__main__':
    CoffreFort()
