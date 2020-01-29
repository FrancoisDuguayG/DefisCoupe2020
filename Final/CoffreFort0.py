
def CoffreFort():
    mot_de_passe = input("Entrez votre mot de passe: ")
    if verifier_mot_de_passe(mot_de_passe):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ## Peut-être que je devrais mieux cacher le mot de passe pour
    ## les prochaine serrure du coffre fort?
    ## Le mot de passe est écris juste en dessus.


def verifier_mot_de_passe(mot_de_passe):
    return mot_de_passe == "M0t_D3_p4sSe_013"


if __name__ == '__main__':
    CoffreFort()
