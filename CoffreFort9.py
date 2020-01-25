import time


def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if (verifierMotDePasse(motDePasse)):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")
        CoffreFort()

    # Le mot de passe est ci-dessous. Est-il prudent de mettre le mot de passe dans le code source?
    # Et si quelqu'un volait notre code source? Ils sauraient notre
    # mot de passe. Hmm ... je vais penser à quelques façons d'améliorer la sécurité
    # sur les autres portes.
    #
    # -Minion # 9567


def verifierMotDePasse(motDePasse):
    return motDePasse == crypto_recur("gaablat")

def crypto_recur(crypto):
    if len(crypto) < 2:
        return crypto
    return crypto_recur(crypto[-1]) + crypto_recur(crypto[:-1])

if __name__ == '__main__':
    CoffreFort()
