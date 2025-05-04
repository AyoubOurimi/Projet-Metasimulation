class Machine_Turing:
    def __init__(self, etats, transition, etat_initial, alphabet={0, 1}):
        """
        Initialise une machine de Turing.

        :param etats: Liste ou ensemble des états possibles.
        :param transition: Dictionnaire des règles de transition.
                           Clé : (état_actuel, symbole_lu)
                           Valeur : (état_suivant, symbole_écrit, direction)
        :param etat_initial: État de départ de la machine.
        :param alphabet: Alphabet d'entrée (par défaut {0,1}).
        """
        self.alphabet = alphabet
        self.alphabet_travail = self.alphabet.union("□")  # alphabet de travail incluant le blanc
        self.etats = set(etats)
        self.transition = dict(transition)
        self.etat_initial = etat_initial
        self.etat_accept = "ACCEPT"  # état d'acceptation
        self.etat_reject = "REJECT"  # état de rejet

    def get_etats(self):
        """Retourne l'ensemble des états de la machine."""
        return self.etats

    def get_transition(self):
        """Retourne le dictionnaire des transitions."""
        return self.transition


def main():
    etats = {"q0", "q1", "ACCEPT", "REJECT"}
    transitions = {("q0", 0): ("q1", 1, "R"), ("q1", 1): ("ACCEPT", 1, "R"), ("q0", 1): ("REJECT", 0, "L")}
    etat_initial = "q0"

    machine = Machine_Turing(etats, transitions, etat_initial)

    print(f"\nEnsemble des états : {machine.get_etats()}")
    print(f"Dictionnaire contenant les transitions : {machine.get_transition()}\n")

if __name__ == "__main__":
    main()