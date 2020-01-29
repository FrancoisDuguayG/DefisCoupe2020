def CoffreFort():
    mot_de_passe = input("Entrez votre mot de passe: ")
    if verifier_mot_de_passe(mot_de_passe):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    ##
    ##
    ##


def verifier_mot_de_passe(mot_de_passe):
    return mot_de_passe == crypto_recur("EluParCetteCrapule")


def crypto_recur(crypto):
    if len(crypto) < 2:
        return crypto
    return crypto_recur(crypto[-1]) + crypto_recur(crypto[0:-1])


if __name__ == '__main__':
    CoffreFort()
