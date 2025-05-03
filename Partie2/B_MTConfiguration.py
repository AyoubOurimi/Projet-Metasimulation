# Question 9 :

class MTConfiguration:
    def __init__(self, bande, pos, etat_courant):
        """
        Initialise une configuration de la machine de Turing.

        :param bande: Dictionnaire représentant la bande (clé = position, valeur = symbole).
        :param pos: Position actuelle de la tête de lecture/écriture.
        :param etat_courant: État courant de la machine.
        """
        self.bande = dict(bande)
        self.pos = pos
        self.etat_courant = etat_courant
        self.symbole_blanc = "□"

    def get_bande(self):
        """Retourne la bande complète sous forme de dictionnaire."""
        return self.bande

    def get_pos(self):
        """Retourne la position actuelle de la tête."""
        return self.pos

    def get_etat_courant(self):
        """Retourne l'état courant de la machine."""
        return self.etat_courant

    def lire_symbole(self):
        """Lit le symbole à la position actuelle."""
        return self.bande.get(self.pos, self.symbole_blanc)

    def ecrire_symbole(self, symbole):
        """Écrit un symbole à la position actuelle."""
        self.bande[self.pos] = symbole

    def __len__(self):
        """Retourne le nombre de cases écrites sur la bande."""
        return len(self.bande)


def main():
    bande = {0: 1, 1: 0, 2: 1}
    pos = 3
    etat = "q0"

    config = MTConfiguration(bande, pos, etat)

    print(f"Bande actuelle : {config.get_bande()}")
    print(f"Position de la tête : {config.get_pos()}")
    print(f"État courant : {config.get_etat_courant()}")

    symbole_lu = config.lire_symbole()
    print(f"Symbole lu à la position {config.get_pos()} : {symbole_lu}")

    print("Écriture du symbole 0 à la position actuelle...")
    config.ecrire_symbole(0)

    print(f"Bande après écriture : {config.get_bande()}")
    print(f"Taille actuelle de la bande : {len(config)}")

if __name__ == "__main__":
    main()
