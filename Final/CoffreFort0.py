
def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if verifierMotDePasse(motDePasse):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ## Peut-être que je devrais mieux cacher le mot de passe pour
    ## les prochaine serrure du coffre fort?
    ## Le mot de passe est écris juste en dessus.


def verifierMotDePasse(motDePasse):
    return motDePasse == "M0t_D3_p4sSe_003"


if __name__ == '__main__':
    CoffreFort()
