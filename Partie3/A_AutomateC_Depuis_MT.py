# Question 13 :

import sys
import os

# ajoute le dossier "Partie1" au chemin d'import
partie1_chemin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Partie1'))
partie2_chemin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Partie2'))
sys.path.append(partie1_chemin)
sys.path.append(partie2_chemin)

from A_AutomateCellulaire import Automate_Cellulaire
from A_MachineTuring import Machine_Turing
from E_Simulation import simule_calcul_automate
from E_MTSimulation import simulation_MT
from C_Lecture_Fichier_MT import lire_MT_mot_via_fichier

def MT_vers_AC(machine_turing):
    """
    Transforme une machine de Turing en un automate cellulaire équivalent.

    L'alphabet, les états et les transitions de la machine de Turing sont utilisés
    pour construire les règles de l'automate cellulaire. Chaque cellule contient
    soit un symbole avec un état (la tête), soit un simple symbole.

    Pour chaque transition (q, s) → (q', s', D) de la machine :
    - la cellule centrale applique l'action (écriture et perte de la tête) ;
    - une cellule voisine devient la nouvelle tête selon la direction D (L, R ou S).

    :param machine_turing: Instance de Machine_Turing
    :return: Instance de Automate_Cellulaire simulant la machine de Turing
    """

    alphabet = machine_turing.alphabet_travail
    transitions_MT = machine_turing.get_transition()
    etats_MT = machine_turing.get_etats() # états de la machine de Turing

    etats_AC = {(q, s) for q in etats_MT.union({'⋆'}) for s in alphabet} # états de l'automate cellulaires
    transitions_AC = {}

    # aucune cellule du triplet ne contient la tête => on recopie juste le symbole central
    for l1 in alphabet:
        for l2 in alphabet:
            for l3 in alphabet:
                transitions_AC[((('⋆', l1), ('⋆', l2), ('⋆', l3)))] = ('⋆', l2)

    # le triplet contient la tête de lecture au centre => on applique la transition de la machine
    for (q, s), (q2, s2, d) in transitions_MT.items():
        for l1 in alphabet:
            for l3 in alphabet:
                # cellule du centre (avec tête) devient normale
                transitions_AC[((('⋆', l1), (q, s), ('⋆', l3)))] = ('⋆', s2)
                if d == 'R':
                    for l4 in alphabet:
                        transitions_AC[((q, s), ('⋆', l3), ('⋆', l4))] = (q2, l3)
                elif d == 'L':
                    for l0 in alphabet:
                        transitions_AC[((('⋆', l0), ('⋆', l1), (q, s)))] = (q2, l0)
                elif d == 'S':
                    transitions_AC[((('⋆', l1), (q, s), ('⋆', l3)))] = (q2, s2)

    return Automate_Cellulaire(etats_AC, transitions_AC)

def main():
    machine, config_init = lire_MT_mot_via_fichier("Assets/exemple_MT.txt")
    bande = config_init.get_bande()
    taille = len(bande)

    mot_AC = [("⋆", "□")]  # padding gauche
    for i in range(taille):
        symbole = bande.get(i, "□")
        if i == 0:
            mot_AC.append((machine.etat_initial, symbole))  # tête sur la première case réelle
        else:
            mot_AC.append(("⋆", symbole))
    mot_AC.append(("⋆", "□"))  # padding droit

    automate_c = MT_vers_AC(machine) # construction de l'automate cellulaire équivalent à la machine de Turing

    etapes = simule_calcul_automate(mot_AC, automate_c, config_pareil = True) # récupération de la liste des étapes de l'automate cellulaire

    for i, config in enumerate(etapes):
        print(f"Étape {i} :", config) # affichage de la configuration de l'automate cellulaire à chaque étape

if __name__ == "__main__":
    main()

