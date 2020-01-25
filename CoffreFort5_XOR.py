def CoffreFort():
    motDePasse = input("Entrez votre mot de passe: ")
    if (verifierMotDePasse(int(motDePasse, 2))):
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
    byte = 0b11001010
    # = int('11001010', 2)
    motDePasseEncrypte = byte ^ motDePasse

    return motDePasseEncrypte == 0b11111111

# 00110101

if __name__ == '__main__':
    CoffreFort()
