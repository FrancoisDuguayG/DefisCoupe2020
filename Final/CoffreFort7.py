
def CoffreFort():
    mot_de_passe = input("Entrez votre mot de passe: ")
    if verifier_mot_de_passe(mot_de_passe):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ## je suis un Wizard de la programmation
    ## Le mot de passe est trop bien cacher!
    ## Pouf!

def verifier_mot_de_passe(mot_de_passe):
    a = "CaD"
    b = "4bra"
    c = "C0C0"
    d = "s3v"
    d = b
    c = a
    a = d
    d = b
    return mot_de_passe == a + c + a


if __name__ == '__main__':
    CoffreFort()
