
def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if verifierMotDePasse(motDePasse):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ## je suis un Wizard de la programmation
    ## Le mot de passe est trop bien cacher!
    ## Pouf!

def verifierMotDePasse(motDePasse):
    a = "CaD"
    b = "abr4"
    c = "C0C0"
    d = "sda"
    d = b
    c = a
    a = d
    d = b
    return motDePasse == a + c + a


if __name__ == '__main__':
    CoffreFort()
