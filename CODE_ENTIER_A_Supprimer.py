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

    with open(nom_fichier, "r", encoding="utf-8") as fichier:

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
    for i in range(-1, len(configuration)+ 1):
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

def simule_calcul_automate_graphique(mot, automate, N_etapes=None, Transi_p=None, Config_pareil=False):
    config = Configuration(mot)
    configs = [config.get_list_etats()]
    etape = 0

    etats_uniques = []
    for e in mot + list(automate.get_etats()) + ["□"]:
        e = str(e)
        if e not in etats_uniques:
            etats_uniques.append(e)

    etat_to_int = {e: i for i, e in enumerate(etats_uniques)}
    int_to_etat = {i: e for e, i in etat_to_int.items()}
    cmap = plt.get_cmap("nipy_spectral")

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))

    while True:
        ancienne = config.get_list_etats()
        config = configuration_suivante(automate, config)
        nouvelle = config.get_list_etats()
        configs.append(nouvelle)
        etape += 1

        # Padding
        max_len = max(len(c) for c in configs)
        configs_padded = []
        for c in configs:
            pad_left = (max_len - len(c)) // 2
            pad_right = max_len - len(c) - pad_left
            configs_padded.append(["□"] * pad_left + c + ["□"] * pad_right)

        # Nettoyage final : lignes puis colonnes
        encoded = np.array([
            [etat_to_int[str(cell)] for cell in row] for row in configs_padded
        ])

        # Supprime lignes 100% "□"
        encoded = encoded[~np.all(encoded == etat_to_int["□"], axis=1)]

        # Supprime colonnes 100% "□"
        encoded = encoded[:, ~np.all(encoded == etat_to_int["□"], axis=0)]

        # Si plus rien à afficher
        if encoded.size == 0:
            print("Tout est vide.")
            break

        data = encoded.T

        # Affichage
        ax.clear()
        im = ax.imshow(data, cmap=cmap, aspect='auto', interpolation='none')

        for y in range(data.shape[0]):
            for x in range(data.shape[1]):
                val = int_to_etat[data[y, x]]
                ax.text(x, y, val, ha='center', va='center', color='white', fontsize=8)

        ax.set_title(f"Évolution – Étape {etape}")
        ax.set_xlabel("Temps")
        ax.set_ylabel("Cellules")
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_yticks(np.arange(data.shape[0]))

        used = np.unique(data)
        legend = [plt.Line2D([0], [0], marker='s', color='w', label=int_to_etat[i],
                  markerfacecolor=im.cmap(im.norm(i)), markersize=10) for i in used]
        ax.legend(handles=legend, bbox_to_anchor=(1.05, 1), loc='upper left')

        fig.canvas.draw()
        plt.pause(0.3)

        if N_etapes is not None and etape >= N_etapes:
            break

        if Transi_p is not None:
            for i in range(len(ancienne)):
                triplet = (
                    ancienne[i - 1] if i > 0 else "□",
                    ancienne[i],
                    ancienne[i + 1] if i < len(ancienne) - 1 else "□"
                )
                if triplet == Transi_p:
                    plt.ioff()
                    plt.show()
                    return configs

        if Config_pareil and nouvelle == ancienne:
            break

    plt.ioff()
    plt.show()
    return configs




#Sert pour la question 7
def ecrire_automate_cyclique_fichier(nom_fichier, alphabet, mot):
    cycle = {alphabet[i]: alphabet[(i + 1) % len(alphabet)] for i in range(len(alphabet))}

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"mot = {''.join(mot)}\n\n")
        for g in alphabet + ["□"]:
            for m in alphabet:
                for d in alphabet + ["□"]:
                    f.write(f"{g} {m} {d} => {cycle[m]}\n")


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

    """ print(simule_calcul_automate([0,0,0,1,0,0,0], A, N_etapes = 5))
    print(simule_calcul_automate([0,0,0,1,0,0,0], A, Transi_p = (1,1,1))) """
    """ print(simule_calcul_automate([0,0,0,1,0,0,0], A, Config_pareil = True)) """  #boucle infini avec l'exemple actuel mais ca marche ;)

    """ print(simule_calcul_automate_graphique([0,0,0,1,0,0,0], A, N_etapes = 1))
    print(simule_calcul_automate_graphique(list("□□aabbbbabca□□"), Automate_Cellulaire(list("aabccbabca"), {("a", "a", "a"): "b",("a", "a", "b"): "c",("a", "a", "c"): "a",("a", "a", "□"): "b",("a", "b", "a"): "c",("a", "b", "b"): "a",("a", "b", "c"): "b",("a", "b", "□"): "c",("a", "c", "a"): "a",("a", "c", "b"): "b",("a", "c", "c"): "c",("a", "c", "□"): "a",("b", "a", "a"): "c",("b", "a", "b"): "a",("b", "a", "c"): "b",("b", "a", "□"): "c",("b", "b", "a"): "a",("b", "b", "b"): "b",("b", "b", "c"): "c",("b", "b", "□"): "a",("b", "c", "a"): "b",("b", "c", "b"): "c",("b", "c", "c"): "a",("b", "c", "□"): "b",("c", "a", "a"): "a",("c", "a", "b"): "b",("c", "a", "c"): "c",("c", "a", "□"): "a",("c", "b", "a"): "c",("c", "b", "b"): "a",("c", "b", "c"): "b",("c", "b", "□"): "c",("c", "c", "a"): "b",("c", "c", "b"): "c",("c", "c", "c"): "a",("c", "c", "□"): "b",("□", "a", "a"): "b",("□", "a", "b"): "c",("□", "a", "c"): "a",("□", "a", "□"): "b",("□", "b", "a"): "a",("□", "b", "b"): "c",("□", "b", "c"): "b",("□", "b", "□"): "a",("□", "c", "a"): "c",("□", "c", "b"): "a",("□", "c", "c"): "b",("□", "c", "□"): "c"}), N_etapes = 5)) """

#Question 7:

    #1. croissance infini

    """ automate, config = lire_automate_mot_via_fichier("croissance_infini.txt")
    print(simule_calcul_automate_graphique(config.get_list_etats(), automate, N_etapes=20)) """
    
    #2. cycle avec alphabet

    alphabet = list("azcdefghijklmnopqrstuvwxy")  #faut que les elmts soit uniques
    mot = list("aocdefghijklmnopqrstuvwxyz")

    ecrire_automate_cyclique_fichier("automate_cyclique.txt", alphabet, mot) #trop de transition fct pour les faire
    automate, config = lire_automate_mot_via_fichier("automate_cyclique.txt")

    simule_calcul_automate_graphique(config.get_list_etats(), automate, N_etapes=30)

    #3. 

    etats = [0, 1]
    transitions = {(g, m, d): 1 - m if g != d else m
                for g in etats for m in etats for d in etats}

    A3 = Automate_Cellulaire(etats, transitions)
    mot3 = [0, 1]*20
    simule_calcul_automate_graphique(mot3, A3, N_etapes=30)

if __name__ == "__main__":
    main()
