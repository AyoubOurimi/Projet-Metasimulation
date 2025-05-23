# Question 7 :

from C_Lecture_Fichier_Automate import lire_automate_mot_via_fichier
from F_Simulation_Graphique import simule_calcul_automate_graphique

def ecrire_automate_cyclique_fichier(nom_fichier, alphabet, mot):
    """
    Génère un fichier décrivant un automate cellulaire cyclique.

    - Le mot initial est écrit en haut du fichier (ex: mot = ABC).
    - L'automate suit une règle cyclique : chaque symbole m ∈ alphabet évolue vers le suivant dans l’ordre.
      Exemple : si alphabet = [A, B, C], alors A→B, B→C, C→A.
    - Pour chaque triplet (g, m, d) avec g, d ∈ alphabet ∪ {"□"} et m ∈ alphabet,
      une règle est écrite sous la forme : g m d => nouveau_m

    :param nom_fichier: Nom du fichier à créer
    :param alphabet: Liste des symboles utilisés par l’automate
    :param mot: Mot initial à insérer en haut du fichier
    """
    cycle = {alphabet[i]: alphabet[(i + 1) % len(alphabet)] for i in range(len(alphabet))}

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"mot = {''.join(mot)}\n\n")
        for g in alphabet + ["□"]:
            for m in alphabet:
                for d in alphabet + ["□"]:
                    f.write(f"{g} {m} {d} => {cycle[m]}\n")


def main():
  # 1. automate à croissance infinie
  print("\n--- Simulation : Croissance infinie ---")

  automate, config = lire_automate_mot_via_fichier("Assets/automate_croissance_infini.txt")
  simule_calcul_automate_graphique(config.get_list_etats(), automate, n_etapes=15)

  # 2. automate cyclique
  print("\n--- Simulation : Automate cyclique ---")

  alphabet = list("ABCDEF")
  mot = list("ACE")
  ecrire_automate_cyclique_fichier("Assets/automate_cyclique.txt", alphabet, mot)  
  automate, config = lire_automate_mot_via_fichier("Assets/automate_cyclique.txt")
  simule_calcul_automate_graphique(config.get_list_etats(), automate, n_etapes=15) 

  # 3. automate qui représente aⁿbⁿ
  print("\n--- Simulation : Automate qui représente aⁿbⁿ ---")
  automate, config = lire_automate_mot_via_fichier("Assets/automate_aⁿbⁿ.txt")
  simule_calcul_automate_graphique(config.get_list_etats(), automate, n_etapes=15)

  # 4. automate qui représente le triangle de Pascal mod 2 (XOR)
  print("\n--- Simulation : Automate qui représente le triangle de Pascal mod 2 ---\n")
  automate, config = lire_automate_mot_via_fichier("Assets/automate_Pascal.txt")
  simule_calcul_automate_graphique(config.get_list_etats(), automate, n_etapes=30)

if __name__ == "__main__":
   main()