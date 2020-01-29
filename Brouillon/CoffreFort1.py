import baseconvert
import threading
from time import sleep

def CoffreFort():

    mot_de_passe = input("Entrez votre mot de passe: ")
    if (verifier_mot_de_passe(mot_de_passe)):
        print("Accès autorisé.")
    else:
        print("Accès refusé!")

    # Le mot de passe est ci-dessous. Est-il prudent de mettre le mot de passe dans le code source?
    # Et si quelqu'un volait notre code source? Ils sauraient notre
    # mot de passe. Hmm ... je vais penser à quelques façons d'améliorer la sécurité
    # sur les autres portes.
    #
    # -Minion # 9567

def verifier_mot_de_passe(mot_de_passe):
    #
    mot_de_passeEncrypte = baseconvert.base(mot_de_passe, 10, 2, string=True)
    return mot_de_passeEncrypte == '10101'

def hello():
    print("hello?")

if __name__ == '__main__':
    t = threading.Timer(10, hello)
    t.start()
    #t.change(2)
    sleep(5)
    print(t.getName())
    CoffreFort()
