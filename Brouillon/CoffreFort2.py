import baseconvert

def CoffreFort():

    motDePasse = input("Entrez votre mot de passe: ")
    if (verifierMotDePasse(motDePasse.upper())):
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
    motDePasseEncrypte = baseconvert.base(motDePasse, 16, 10, string=True)
    return motDePasseEncrypte == "42"


if __name__ == '__main__':
    try:
        CoffreFort()
    except:
        print("ERREUR \n.. \nFERMETURE DU COFFRE FORT")
