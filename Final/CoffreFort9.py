
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
    bank = [1, 2, 3, 4, 5, 6, 7]
    crypto = 0
    for mot in bank:
        crypto += bank[(3 * mot) % 6]
    return motDePasse == crypto


if __name__ == '__main__':
    CoffreFort()
