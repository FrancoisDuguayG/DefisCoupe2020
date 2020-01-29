
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
    return (len(mot_de_passe) == 10 and
            mot_de_passe[7] == "R" and
            mot_de_passe[2] == "N" and
            mot_de_passe[4] == "o" and
            mot_de_passe[8] == "3" and
            mot_de_passe[0] == "b" and
            mot_de_passe[3] == "_" and
            mot_de_passe[1] == "0" and
            mot_de_passe[9] == "?" and
            mot_de_passe[5] == "R" and
            mot_de_passe[6] == "d")


if __name__ == '__main__':
    CoffreFort()
