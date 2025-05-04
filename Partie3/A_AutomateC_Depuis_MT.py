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

import sys
import os

# Ajout du chemin vers Partie1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Partie1')))
from A_AutomateCellulaire import Automate_Cellulaire


def construire_automate_depuis_MT(machine):
    """
    Construit un automate cellulaire qui simule une machine de Turing.
    Chaque cellule contient (symbole, état) où l'état est None ou un état MT si la tête est dessus.
    """
    etats_MT = list(machine.get_etats()) + [machine.etat_accept, machine.etat_reject]
    symboles = list(machine.alphabet.union({'□'}))

    etats_automate = []
    transitions = {}

    for s in symboles:
        for e in [None] + etats_MT:
            etats_automate.append((s, e))

    for g in etats_automate:
        for c in etats_automate:
            for d in etats_automate:
                s_g, e_g = g
                s_c, e_c = c
                s_d, e_d = d

                # Si déjà en état terminal : figé
                if e_c in (machine.etat_accept, machine.etat_reject):
                    transitions[(g, c, d)] = c
                    continue

                # Si la tête est ici
                if e_c is not None:
                    cle = (e_c, s_c)
                    if cle in machine.get_transition():
                        e_suiv, s_ecrit, direction = machine.get_transition()[cle]

                        # Si état final, on reste dessus
                        if e_suiv in (machine.etat_accept, machine.etat_reject):
                            transitions[(g, c, d)] = (s_ecrit, e_suiv)
                            continue

                        # Sinon : écrire et perdre la tête
                        transitions[(g, c, d)] = (s_ecrit, None)
                        continue

                # Si tête vient de gauche (droite après écriture)
                if e_g is not None:
                    cle = (e_g, s_g)
                    if cle in machine.get_transition():
                        e_suiv, _, direction = machine.get_transition()[cle]
                        if direction == 'R':
                            transitions[(g, c, d)] = (s_c, e_suiv)
                            continue

                # Si tête vient de droite (gauche après écriture)
                if e_d is not None:
                    cle = (e_d, s_d)
                    if cle in machine.get_transition():
                        e_suiv, _, direction = machine.get_transition()[cle]
                        if direction == 'L':
                            transitions[(g, c, d)] = (s_c, e_suiv)
                            continue

                # Par défaut, rien ne change
                transitions[(g, c, d)] = c

    return Automate_Cellulaire(etats_automate, transitions)


def test_MT_vs_automate(mot, machine, n_etapes=20):
    automate = construire_automate_depuis_MT(machine)

    bande_init = [(sym, None) for sym in mot]
    bande_init[0] = (bande_init[0][0], machine.etat_initial)

    configs_auto = simule_calcul_automate(bande_init, automate, N_etapes=n_etapes)
    resultat_MT = simulation_MT(mot, machine)

    print("États simulés par automate :")
    for ligne in configs_auto:
        print(ligne)

    print(f"\nRésultat MT : {'Accepté' if resultat_MT else 'Rejeté'}")
    return configs_auto

if __name__ == "__main__":
    machine, _ = lire_MT_mot_via_fichier("Assets/exemple_MT.txt")
    test_MT_vs_automate(list("1100"), machine)
