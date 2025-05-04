# Question 10 :

from A_MachineTuring import Machine_Turing
from B_MTConfiguration import MTConfiguration

def lire_MT_mot_via_fichier(nom_fichier):
    """
    Lit un fichier texte décrivant une machine de Turing et un mot d'entrée.

    Le fichier doit contenir :
    - une ligne commençant par 'mot =' pour définir le mot (liste de symboles)
    - une ligne 'etat initial =' pour définir l'état initial
    - des lignes de transition de la forme 'etat symbole_lu => etat_suivant symbole_ecrit direction'

    :param nom_fichier: Chemin vers le fichier
    :return: Tuple (Machine_Turing, MTConfiguration)
    """
    etats = set()
    transitions = {}
    mot = []
    etat_initial = None

    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            if not ligne:
                continue

            if ligne.startswith("mot ="):
                mot = list(ligne.split("=", 1)[1].strip()) # récupère le mot
            elif ligne.startswith("état initial ="): # récupère l'état initial
                etat_initial = ligne.split("=", 1)[1].strip()
            elif '=>' in ligne:
                gauche, droite = ligne.split("=>")
                cle = tuple(gauche.strip().split())           # (etat, symbole_lu)
                valeur = tuple(droite.strip().split())        # (etat_suivant, symbole_ecrit, direction)
                transitions[cle] = valeur

                etats.add(cle[0])           # ajoute l'état actuel a l'ensemble d'états
                etats.add(valeur[0])        # ajoute l'état suivant a l'ensemble d'états

    # création de la bande initiale : position i -> symbole
    bande = {i: sym for i, sym in enumerate(mot)}

    return Machine_Turing(etats, transitions, etat_initial, alphabet = set(mot)), MTConfiguration(bande, 0, etat_initial)

def main():
    machine, config = lire_MT_mot_via_fichier("Assets/exemple_MT.txt")

    print(f"\nInstance de Machine_Turing : {machine}")
    print(f"Instance de MTConfiguration : {config}")

    print(f"États de la machine : {machine.get_etats()}")
    print(f"Transitions de la machine : {machine.get_transition()}")

    print(f"Bande initiale : {config.get_bande()}")
    print(f"Position initiale de la tête : {config.get_pos()}")
    print(f"État initial : {config.get_etat_courant()}\n")

if __name__ == "__main__":
    main()

