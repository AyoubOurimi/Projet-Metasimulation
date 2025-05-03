# Question 11 :

from A_MachineTuring import Machine_Turing
from B_MTConfiguration import MTConfiguration
from C_Lecture_Fichier_MT import lire_MT_mot_via_fichier

def configuration_suivante_MT(machine, configuration):
    """
    Calcule la configuration suivante à partir d'une configuration actuelle et
    d'une machine de Turing, sans modifier l'ancienne configuration.

    :param machine: Instance de Machine_Turing
    :param configuration: Instance de MTConfiguration
    :return: Nouvelle instance de MTConfiguration
    """
    pos = configuration.get_pos()
    etat_courant = configuration.get_etat_courant()
    symbole_lu = configuration.lire_symbole()

    # création de la clé pour accéder à la transition s'il elle existe
    cle = (etat_courant, symbole_lu)
    transition = machine.get_transition().get(cle)

    if transition is None:
        raise ValueError(f"Aucune transition définie pour {cle}")

    etat_suivant, symbole_ecrit, direction = transition

    # création d'une copie de la bande (pour ne pas modifier l'originale)
    nouvelle_bande = dict(configuration.get_bande())
    nouvelle_bande[pos] = symbole_ecrit  

    # déplacement de la tête
    if direction == "R":
        pos += 1
    elif direction == "L":
        pos -= 1
    elif direction == "S":
        pass
    else:
        raise ValueError("Direction invalide : doit être 'L', 'R' ou 'S'")

    # ajout d'un symbole blanc si la position est hors de la bande
    if pos not in nouvelle_bande:
        nouvelle_bande[pos] = configuration.symbole_blanc

    return MTConfiguration(nouvelle_bande, pos, etat_suivant)

def main():
    machine, config = lire_MT_mot_via_fichier("Assets/exemple_MT.txt")
    config_suivante = configuration_suivante_MT(machine, config)

    print(f"La configuration suivante de la bande {config.get_bande()} avec la tête en position {config.get_pos()} et l'état courant {config.get_etat_courant()} devient : ")
    print(f"bande : {config_suivante.get_bande()}, tête en position : {config_suivante.get_pos()}, état courant : {config_suivante.get_etat_courant()}.")

if __name__ == "__main__":
    main()