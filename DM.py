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
                
    automate = Automate_Cellulaire(etats, transitions)
    configuration = Configuration(mot)

    return automate, configuration

#Question 4 :
def configuration_suivante(automate, configuration):
    config_suivante = []
    for i in range(len(configuration)):
        gauche, milieu, droite = configuration.get_index_etat(i-1), configuration.get_index_etat(i), configuration.get_index_etat(i+1)
        config_suivante.append(automate.get_etat_apres_transition(gauche, milieu, droite))
        print(config_suivante)
    
    return Configuration(config_suivante)

#Question 5 :
def simule_calcul_automate(mot, automate, ):
    pass
        

    
        
    

""" BELEK ON AJOUTE DES SURCHARGE D'OPERATEUR  """

#on fait les tests dans le main avec comme transi la regle 110 comme dans le dm
def main():
    A = Automate_Cellulaire([0,1], {(1, 1, 1): 0, (1, 1, 0): 1, (1, 0, 1): 1, (1, 0, 0): 0, (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0})
    
    """ print(A.etats)

    print(A.transition)

    print(A.get_etat_apres_transition(0,1,1))

    question3 = lire_automate_mot_via_fichier("question3.txt")
    print(question3) """

    C = Configuration([0,1,1,0,1,0,0,1,1])
    question4 = configuration_suivante(A,C)
    print(question4.l_etats)


if __name__ == "__main__":
    main()