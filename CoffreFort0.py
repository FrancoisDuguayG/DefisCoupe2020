import time


def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if (verifierMotDePasse(motDePasse)):
        time.sleep(2)
        print("Accès autorisé.")
    else:
        time.sleep(2)
        print("Accès refusé!")
        CoffreFort()

    # Le mot de passe est ci-dessous. Est-il prudent de mettre le mot de passe dans le code source?
    # Et si quelqu'un volait notre code source? Ils sauraient notre
    # mot de passe. Hmm ... je vais penser à quelques façons d'améliorer la sécurité
    # sur les autres portes.
    #
    # -Minion # 9567

def verifierMotDePasse(motDePasse):
    return motDePasse == "M0t_D3_p4sSe_003"


if __name__ == '__main__':
    CoffreFort()
