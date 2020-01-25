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
    if len(motDePasse) != 10:
        return False
    motDePasseEncrypte = ""

    for i in range(0, 5):
        motDePasseEncrypte += motDePasse[i]

    for i in range(9, 4, -1):
        motDePasseEncrypte += motDePasse[i]

    print(motDePasseEncrypte)
    return motDePasseEncrypte == "abcdefghij"

# abcdejihgf

if __name__ == '__main__':
    CoffreFort()
