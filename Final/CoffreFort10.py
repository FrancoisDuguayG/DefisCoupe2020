
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
    print(crypto_recur("elu_par_cette_crapule"))
    return motDePasse == crypto_recur("elu_par_cette_crapule")

def crypto_recur(crypto):
    if len(crypto) < 2:
        return crypto
    return crypto_recur(crypto[-1]) + crypto_recur(crypto[:-1])

if __name__ == '__main__':
    CoffreFort()
