# Question 3 :

from A_AutomateCellulaire import Automate_Cellulaire
from B_Configuration import Configuration

def lire_automate_mot_via_fichier(nom_fichier):
    """
    Lit un fichier texte contenant :
    - une ligne commençant par 'mot =' définissant l'état initial
    - des lignes définissant les transitions : 'gauche milieu droite => nouvelle_valeur'

    :param nom_fichier: Chemin vers le fichier texte
    :return: Tuple (Automate_Cellulaire, Configuration)
    """
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
                gauche, droite = ligne.split("=>") # sépare la partie gauche et droite de la transition 
                cle_triplet = tuple(gauche.strip().split())
                valeur = droite.strip()
                transitions[cle_triplet] = valeur # récupère les transitions

                # ajoute tous les états vus
                etats.update(cle_triplet)
                etats.add(valeur)

    return Automate_Cellulaire(etats, transitions), Configuration(mot)

def main():
    automate, config = lire_automate_mot_via_fichier("Assets/exemple_Automate.txt")

    print(f"Instance d'Automate_Cellulaire {automate}")
    print(f"Instance de Configuration {config}")

    print(f"Etats : {automate.get_etats()}")
    print(f"Transitions : {automate.get_transition()}")

    print(f"Le mot en liste d'état est : {config.get_list_etats()}")

if __name__ == "__main__":
    main()