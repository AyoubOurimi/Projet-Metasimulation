# Question 1 :

class Automate_Cellulaire:
    def __init__(self, etats, transition):
        """
        Initialise l'automate cellulaire.

        :param etats: Liste ou ensemble des états possibles.
        :param transition: Dictionnaire des règles de transition.
                           Clé : (état_gauche, état_central, état_droit)
                           Valeur : nouvel état du centre à t+1
        """
        self.etats = set(etats)
        self.transition = dict(transition)

        # transition par défaut
        self.transition[("□", "□", "□")] = "□"

    def get_etats(self):
        """Retourne l'ensemble des états possibles."""
        return self.etats

    def get_transition(self):
        """Retourne le dictionnaire des règles de transition."""
        return self.transition

    def get_etat_apres_transition(self, gauche, milieu, droite):
        """
        Applique la règle de transition sur un triplet (gauche, milieu, droite).

        :param gauche: État de la cellule gauche
        :param milieu: État de la cellule centrale
        :param droite: État de la cellule droite
        :return: Nouvel état de la cellule centrale
        """
        return self.transition.get((gauche, milieu, droite), milieu)
    
def main():
    automate = Automate_Cellulaire([0,1], {(1, 1, 1): 0, (1, 1, 0): 1, (1, 0, 1): 1, (1, 0, 0): 0, (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0})

    print(f"\nEnsemble des états possibles : {automate.get_etats()}")

    print(f"Dictionnaire contenant les transitions : {automate.get_transition()}")

    triplet = (0,1,1)
    print(f"Le triplet {triplet} renvoie après transition : {automate.get_etat_apres_transition(triplet[0],triplet[1],triplet[2])}\n")

if __name__ == "__main__":
    main()
