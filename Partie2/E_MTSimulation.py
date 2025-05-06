# Question 12 :

from A_MachineTuring import Machine_Turing
from B_MTConfiguration import MTConfiguration
from C_Lecture_Fichier_MT import lire_MT_mot_via_fichier
from D_MTConfig_Suivante import configuration_suivante_MT

def simulation_MT(mot, machine) :
    """
    Simule l'exécution d'une machine de Turing sur un mot donné.

    :param mot: Liste de symboles représentant le mot d'entrée
    :param machine: Instance de Machine_Turing
    :return: True si le mot est accepté, False s'il est rejeté
    """
    mot = list(mot)
    bande = {i: sym for i, sym in enumerate(mot)}
    conf = MTConfiguration(bande, 0, etat_courant=machine.etat_initial)
    configs = [(conf.get_bande(), conf.get_pos(), conf.get_etat_courant())]

    # boucle principale de la machine de Turing jusqu'à un état d'acceptation ou de rejet
    while True:
        # vérifier si la configuration actuelle est un état d'acceptation ou de rejet
        if conf.get_etat_courant() == machine.etat_accept:
            print(f"\nLa liste des configurations est : {configs}") # permet de voir les configurations successives
            return True
        elif conf.get_etat_courant() == machine.etat_reject:
            print(f"La liste des configurations est : {configs}") # permet de voir les configurations successives
            return False

        # recupérer la configuration suivante
        conf = configuration_suivante_MT(machine, conf)
        configs.append((conf.get_bande(), conf.get_pos(), conf.get_etat_courant()))

def main():
    mot_accept = "1100" # exemple de mot
    machine, _ = lire_MT_mot_via_fichier("Assets/exemple_MT_pair.txt") # MT qui verifie le nombre de 1 est pair
    resultat_accept = simulation_MT(mot_accept, machine)
    print(f"\nLe mot {''.join(mot_accept)} est {'accepté' if resultat_accept else 'rejeté'} par la machine.")

    mot_reject = "11100" # exemple de mot
    machine, _ = lire_MT_mot_via_fichier("Assets/exemple_MT_pair.txt") # MT qui verifie le nombre de 1 est pair
    resultat_reject = simulation_MT(mot_reject, machine)
    print(f"Le mot {''.join(mot_reject)} est {'accepté' if resultat_reject else 'rejeté'} par la machine.\n")

if __name__ == "__main__":
    main()
 