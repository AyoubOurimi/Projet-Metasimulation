# Question 2 :

class Configuration:
    def __init__(self, l_etats):
        """
        Initialise une configuration de l'automate.

        :param l_etats: Liste des états des cellules à t donné
        """
        self.l_etats = list(l_etats)
        self.valeur_par_defaut = "□" 

    def get_list_etats(self):
        """Retourne la liste des états actuels."""
        return self.l_etats

    def get_index_etat(self, index):
        """
        Retourne l'état de la cellule à l'index donné.

        :param index: Position de la cellule
        :return: L'état correspondant, ou la valeur par défaut si hors limites
        """
        if index < 0 or index >= len(self.l_etats):
            return self.valeur_par_defaut
        return self.l_etats[index]

    def __len__(self):
        """Permet d'utiliser len(configuration) directement."""
        return len(self.l_etats)
    
def main():
    C = Configuration([0, 1, 1, 0, 1, 0, 0, 1, 1])

    print(f"Liste des états : {C.get_list_etats()}")

    index_test1 = 3
    print(f"État à l'index {index_test1} : {C.get_index_etat(index_test1)}")

    index_test2 = -2
    print(f"État à l'index {index_test2} (hors limites) : {C.get_index_etat(index_test2)}")

    index_test3 = 20
    print(f"État à l'index {index_test3} (hors limites) : {C.get_index_etat(index_test3)}")

    print(f"Longueur de la configuration : {len(C)}")

if __name__ == "__main__":
    main()
