# Question 1 :
class Automate_Cellulaire:
    def __init__(self, etats, transition):
        self.etats = set(etats)
        self.transition = dict(transition) #forme de transition lorsqu'on appelle : {(gauche, milieu, droite): VALEUR milieur en t+1}

        #ajout transition par defaut: f(□,□,□) = □
        self.transition[("□", "□", "□")] = "□"

    def get_etats(self):
        return self.etats
    
    def get_transition(self):
        return self.transition
    
    def get_etat_apres_transition(self, gauche, milieu, droite):
        return self.transition.get((gauche, milieu, droite), milieu)
    

#Question 2 :
class Configuration:
    def __init__(self, l_etats):
        self.l_etats = list(l_etats)
        self.valeur_par_defaut = "□"

    def get_list_etats(self):
        return self.l_etats
    
    def get_index_etat(self, index):
        if index < 0 or index > len(self.l_etats) - 1:
            return self.valeur_par_defaut
        else:
            return self.l_etats[index]
    
    #surcharge utile
    def __len__(self):
        return len(self.l_etats)


#Question 3 :
def lire_automate_mot_via_fichier(nom_fichier):
    etats = set()
    transitions = {}
    mot = []

    with open(nom_fichier, "r") as fichier:

        for ligne in fichier:
            ligne = ligne.strip()
            if not ligne:
                continue
            if ligne.startswith("mot ="):
                mot = list(ligne.split("=", 1)[1].strip())
            elif '=>' in ligne:
                gauche, droite = ligne.split("=>")
                cle_triplet = tuple(gauche.strip().split())
                valeur = droite.strip()
                transitions[cle_triplet] = valeur

                #on ajoute les etats vu pdt la boucle
                etats.update(cle_triplet)
                etats.add(valeur)
                
    return Automate_Cellulaire(etats, transitions), Configuration(mot)


#Question 4 :
def configuration_suivante(automate, configuration):
    config_suivante = []
    for i in range(len(configuration)):
        gauche, milieu, droite = configuration.get_index_etat(i-1), configuration.get_index_etat(i), configuration.get_index_etat(i+1)
        config_suivante.append(automate.get_etat_apres_transition(gauche, milieu, droite))
    
    return Configuration(config_suivante)

#Question 5 :
def simule_calcul_automate(mot, automate, N_etapes = None, Transi_p = None, Config_pareil = False):
    Config = Configuration(mot)
    l_configs = [Config.get_list_etats()]
    etape = 0

    while True:
        ancienne_config = Config.get_list_etats()
        Config = configuration_suivante(automate, Config)
        nouvelle_config = Config.get_list_etats()
        l_configs.append(nouvelle_config)
        etape += 1

        #mode 1
        if N_etapes is not None and etape >= N_etapes:
            break

        #mode 2
        if Transi_p is not None:
            for i in range(len(ancienne_config)):
                triplet = (ancienne_config[i - 1] if i > 0 else 0, ancienne_config[i], ancienne_config[i + 1] if i < len(ancienne_config) - 1 else 0)
                if triplet == Transi_p:
                    return l_configs

        #mode 3
        if Config_pareil and nouvelle_config == ancienne_config:
            break

    return l_configs


#Question 6 :
import matplotlib.pyplot as plt
import numpy as np
import time

def simule_calcul_automate_graphique(mot, automate, N_etapes=None, Transi_p=None, Config_pareil=False):
    Config = Configuration(mot)
    l_configs = [Config.get_list_etats()]
    etape = 0

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))

    while True:
        ancienne_config = Config.get_list_etats()
        Config = configuration_suivante(automate, Config)
        nouvelle_config = Config.get_list_etats()
        l_configs.append(nouvelle_config)
        etape += 1

        data = np.array(l_configs).T  # chaque ligne = une cellule, chaque colonne = un temps

        ax.clear()
        im = ax.imshow(data, cmap='Greys', aspect='auto', interpolation='none')

        # delimiter chaque cellule
        ax.set_xticks(np.arange(data.shape[1] + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(data.shape[0] + 1) - 0.5, minor=True)
        ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.8)
        ax.tick_params(which="minor", bottom=False, left=False)

        # ajouts visuels
        ax.set_title(f"Évolution de l'automate – Étape {etape}")
        ax.set_xlabel("Temps")
        ax.set_ylabel("Cellules")
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_yticks(np.arange(data.shape[0]))

        fig.canvas.draw()
        plt.pause(0.4)

        if N_etapes is not None and etape >= N_etapes:
            break

        if Transi_p is not None:
            for i in range(len(ancienne_config)):
                triplet = (
                    ancienne_config[i - 1] if i > 0 else 0,
                    ancienne_config[i],
                    ancienne_config[i + 1] if i < len(ancienne_config) - 1 else 0
                )
                if triplet == Transi_p:
                    plt.ioff()
                    plt.show()
                    return l_configs

        if Config_pareil and nouvelle_config == ancienne_config:
            break

    plt.ioff()
    plt.show()
    return l_configs


""" BELEK ON CONSIDERE QUE LES VALEUR INEXISTANT C'EST □ """

#on fait les tests dans le main avec comme transi la regle 110 comme dans le dm
def main():
    A = Automate_Cellulaire([0,1], {(1, 1, 1): 0, (1, 1, 0): 1, (1, 0, 1): 1, (1, 0, 0): 0, (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0})
    
    """ print(A.get_etats())

    print(A.get_transition())

    print(A.get_etat_apres_transition(0,1,1))

    question3 = lire_automate_mot_via_fichier("question3.txt")
    print(question3[0].get_transition()) """

    C = Configuration([0,1,1,0,1,0,0,1,1])
    """ question4 = configuration_suivante(A,C)
    print(question4.l_etats) """

    print(simule_calcul_automate([0,0,0,1,0,0,0], A, N_etapes = 5))
    print(simule_calcul_automate([0,0,0,1,0,0,0], A, Transi_p = (1,1,1)))
    """ print(simule_calcul_automate([0,0,0,1,0,0,0], A, Config_pareil = True)) """  #boucle infini avec l'exemple actuel mais ca marche ;)

    print(simule_calcul_automate_graphique([0,0,0,1,0,0,0], A, N_etapes = 5))
    print(simule_calcul_automate_graphique([0,0,0,1,0,0,0], A, Transi_p = (1,1,1)))


if __name__ == "__main__":
    main()