def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if (verifierMotDePasse(motDePasse)):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")

    # Le mot de passe est ci-dessous. Est-il prudent de mettre le mot de passe dans le code source?
    # Et si quelqu'un volait notre code source? Ils sauraient notre
    # mot de passe. Hmm ... je vais penser à quelques façons d'améliorer la sécurité
    # sur les autres portes.
    #
    # -Minion # 9567


def verifierMotDePasse(motDePasse):
    return (len(motDePasse) == 10 and
            motDePasse[7] == "R" and
            motDePasse[2] == "N" and
            motDePasse[4] == "o" and
            motDePasse[8] == "3" and
            motDePasse[0] == "b" and
            motDePasse[3] == "_" and
            motDePasse[1] == "0" and
            motDePasse[9] == "?" and
            motDePasse[5] == "R" and
            motDePasse[6] == "d")

#b0N_oRdR3?

if __name__ == '__main__':
    CoffreFort()
