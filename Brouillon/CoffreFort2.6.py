
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
    liste = ["a","s"]


if __name__ == '__main__':
    CoffreFort()
