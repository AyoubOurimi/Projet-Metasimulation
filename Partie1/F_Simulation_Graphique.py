# Question 6 :

import matplotlib.pyplot as plt
import numpy as np

from A_AutomateCellulaire import Automate_Cellulaire
from B_Configuration import Configuration
from D_Config_Suivante import configuration_suivante_graph

def simule_calcul_automate_graphique(mot, automate, n_etapes=None, transi_p=None, config_pareil=False):
    """
    Simule et affiche graphiquement l'évolution d'un automate cellulaire.

    Affiche chaque étape avec une légende, une carte de couleurs et les états affichés dans les cellules.

    :param mot: Mot initial (liste d'états)
    :param automate: Instance d'Automate_Cellulaire
    :param n_etapes: Nombre d'étapes maximum (optionnel)
    :param transi_p: Triplet de transition déclencheur d'arrêt (optionnel)
    :param config_pareil: Si True, arrêt si la configuration ne change plus
    :return: Liste des configurations successives
    """
    config = Configuration(mot)
    configs = [config.get_list_etats()]
    etape = 0

    # créer le mapping entre états et entiers
    etats_uniques = []
    for e in mot + list(automate.get_etats()) + ["□"]:
        e = str(e)
        if e not in etats_uniques:
            etats_uniques.append(e)

    etat_to_int = {e: i for i, e in enumerate(etats_uniques)} # mapping entre états et entiers
    int_to_etat = {i: e for e, i in etat_to_int.items()} # inverse du mapping
    cmap = plt.get_cmap("nipy_spectral") # carte de couleurs pour les états

    plt.ion() # active le mode interactif
    fig, ax = plt.subplots(figsize=(10, 6)) # crée une figure et un axe

    while True:
        ancienne = config.get_list_etats()
        config = configuration_suivante_graph(automate, config)
        nouvelle = config.get_list_etats()
        configs.append(nouvelle)
        etape += 1

        # ajoute des cellules vides pour le padding
        max_len = max(len(c) for c in configs)
        configs_padded = []
        for c in configs:
            pad_gauche = (max_len - len(c)) // 2
            pad_droite = max_len - len(c) - pad_gauche
            configs_padded.append(["□"] * pad_gauche + c + ["□"] * pad_droite)

        # transforme les configurations en tableau d'entiers
        tableau_etats = np.array([[etat_to_int[str(cell)] for cell in row] for row in configs_padded])

        # supprime les lignes 100% vides
        tableau_etats = tableau_etats[~np.all(tableau_etats == etat_to_int["□"], axis=1)]
        # supprime les colonnes 100% vides
        tableau_etats = tableau_etats[:, ~np.all(tableau_etats == etat_to_int["□"], axis=0)]

        if tableau_etats.size == 0:
            print("tout est vide.")
            break

        ax.clear() # efface l'axe pour la nouvelle étape
        im = ax.imshow(tableau_etats, cmap=cmap, aspect='auto', interpolation='none') # affiche le tableau d'états

        # ajoute les valeurs des états dans les cellules
        for y in range(tableau_etats.shape[0]):
            for x in range(tableau_etats.shape[1]):
                val = int_to_etat[tableau_etats[y, x]]
                ax.text(x, y, val, ha='center', va='center', color='white', fontsize=8)

        ax.set_title(f"évolution – étape {etape}") # titre de la figure 
        ax.set_xlabel("cellules") 
        ax.set_ylabel("temps")
        ax.set_xticks(np.arange(tableau_etats.shape[1])) 
        ax.set_yticks(np.arange(tableau_etats.shape[0]))

        # ajout d' une légende pour les états
        etats_utilisés = np.unique(tableau_etats)
        legende = [plt.Line2D([0], [0], marker='s', color='w', label=int_to_etat[i],markerfacecolor=im.cmap(im.norm(i)), markersize=10) for i in etats_utilisés]
        ax.legend(handles=legende, bbox_to_anchor=(1.05, 1), loc='upper left')

        fig.canvas.draw()
        plt.pause(0.3)

        if n_etapes is not None and etape >= n_etapes:
            break

        if transi_p is not None:
            for i in range(len(ancienne)):
                triplet = (
                    ancienne[i - 1] if i > 0 else "□",
                    ancienne[i],
                    ancienne[i + 1] if i < len(ancienne) - 1 else "□"
                )
                if triplet == transi_p:
                    plt.ioff()
                    plt.show()
                    return configs

        if config_pareil and nouvelle == ancienne:
            break

    plt.ioff()
    plt.show()

    return configs