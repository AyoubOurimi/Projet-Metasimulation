# Question 5 :

from A_AutomateCellulaire import Automate_Cellulaire
from B_Configuration import Configuration
from D_Config_Suivante import configuration_suivante

def simule_calcul_automate(mot, automate, n_etapes=None, transi_p=None, config_pareil=False):
    """
    Simule l'évolution de l'automate à partir d'un mot initial.

    Modes d'arrêt :
    - N_etapes : arrêt après un nombre donné d'étapes
    - Transi_p : arrêt dès qu'une transition particulière est rencontrée
    - Config_pareil : arrêt dès qu'une configuration se répète

    :param mot: Mot initial (liste d'états)
    :param automate: Instance de Automate_Cellulaire
    :param n_etapes: (optionnel) Nombre maximum d'étapes
    :param transi_p: (optionnel) Triplet de transition déclencheur d'arrêt
    :param config_pareil: (optionnel) Booléen pour arrêt si configuration stable
    :return: Liste des configurations successives
    """
    Config = Configuration(mot)
    l_configs = [Config.get_list_etats()]
    etape = 0

    while True:
        ancienne_config = Config.get_list_etats() # récupère la configuration actuelle
        Config = configuration_suivante(automate, Config) # calcule la configuration suivante
        nouvelle_config = Config.get_list_etats() # récupère la nouvelle configuration
        l_configs.append(nouvelle_config) # ajoute la nouvelle configuration à la liste
        etape += 1

        if n_etapes is not None and etape >= n_etapes:
            break

       # vérifie si la transition actuelle est égale à la transition donnée
        if transi_p is not None:
            for i in range(len(ancienne_config)):
                triplet = (
                    ancienne_config[i - 1] if i > 0 else "□",
                    ancienne_config[i],
                    ancienne_config[i + 1] if i < len(ancienne_config) - 1 else "□"
                )
                if triplet == transi_p:
                    return l_configs

        # vérifie si la configuration actuelle est égale à la nouvelle configuration
        if config_pareil and nouvelle_config == ancienne_config:
            break

    return l_configs

def main():
    automate = Automate_Cellulaire([0,1], {(1, 1, 1): 0, (1, 1, 0): 1, (1, 0, 1): 1, (1, 0, 0): 0, (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0})

    print(f"\nSimulation avec mode -> [n_etapes] : {simule_calcul_automate([0,0,0,1,0,0,0], automate, n_etapes = 5)}")
    print(f"Simulation avec mode -> [transi_p] : {simule_calcul_automate([0,0,0,1,0,0,0], automate, transi_p = (1,1,1))}") 
    print(f"Simulation avec mode -> [config_pareil] : {simule_calcul_automate([0,0,1,0,0], automate, config_pareil = True)}")

    # ca va simuler le mode tq on a le plus court nombre de figurations dans la liste
    print(f"Simulation avec tous les 3 modes : {simule_calcul_automate([0,0,0,1,0,0,0], automate, n_etapes = 5, transi_p = (1,1,1), config_pareil = True)}\n") 


if __name__ == "__main__":
    main()