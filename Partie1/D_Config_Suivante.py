# Question 4 :

from A_AutomateCellulaire import Automate_Cellulaire
from B_Configuration import Configuration

def configuration_suivante(automate, configuration):
    """
    Calcule la configuration suivante en appliquant les règles de transition à chaque cellule.

    :param automate: Instance d'Automate_Cellulaire
    :param configuration: Instance de Configuration
    :return: Nouvelle Configuration
    """
    config_suivante = []

    for i in range(len(configuration)):
        gauche = configuration.get_index_etat(i-1)
        milieu = configuration.get_index_etat(i)
        droite = configuration.get_index_etat(i+1)
        
        nouveau_etat = automate.get_etat_apres_transition(gauche, milieu, droite)
        config_suivante.append(nouveau_etat)

    return Configuration(config_suivante)


# UTILE POUR LE PADDING POUR BIEN MONTRER GRAPHIQUEMENT LE AUTOMATE SIMULANT UNE CROISSANCE INFINI --> AVEC DU PADDING 
def configuration_suivante_graph(automate, configuration):
    """
    Calcule la configuration suivante en appliquant les règles de transition à chaque cellule. (POUR LE GRAPHIQUE --> PADDING)

    :param automate: Instance d'Automate_Cellulaire
    :param configuration: Instance de Configuration
    :return: Nouvelle Configuration
    """
    config_suivante = []

    for i in range(-1, len(configuration) + 1):
        # récupère les états gauche, milieu et droite en tenant compte du padding
        gauche = configuration.get_index_etat(i-1)
        milieu = configuration.get_index_etat(i)
        droite = configuration.get_index_etat(i+1)
        
        nouveau_etat = automate.get_etat_apres_transition(gauche, milieu, droite)
        config_suivante.append(nouveau_etat)

    return Configuration(config_suivante)


def main():
    automate = Automate_Cellulaire([0,1], {(1, 1, 1): 0, (1, 1, 0): 1, (1, 0, 1): 1, (1, 0, 0): 0, (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0})
    config = Configuration([0,1,1,0,1,0,0,1,1])

    config_suivante = configuration_suivante(automate, config)
    print(f"\nLa configuration suivante de cette configuration {config.l_etats} est : {config_suivante.l_etats}\n")

if __name__ == "__main__":
    main()