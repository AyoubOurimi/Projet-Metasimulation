# 🧠 Projet : MetaSimulation

## 📁 Organisation du projet

Le projet est divisé en trois grandes parties, chacune correspondant à une série de questions sur les automates cellulaires et les machines de Turing.

```
Projet-Metasimulation/
├── Partie1/         # Automates cellulaires
├── Partie2/         # Machines de Turing
├── Partie3/         # Simulation MT avec AC + Raisonnement théorique
├── Assets/          # Fichiers .txt de configuration (automates et machines)
├── Makefile         # Lancement automatique des questions
└── README.md        # Ce fichier
```

---

## ▶️ Lancer le projet

Vous pouvez exécuter automatiquement toutes les parties en ligne de commande :

```bash
make
```

Ou exécuter une partie spécifique :

```bash
make partie1
make partie2
make partie3
```

---

## 🧩 Contenu par Partie

### 🔹 Partie 1 – Automates cellulaires

- Mise en place des structures de données pour représenter un automate cellulaire
- Lecture de fichiers contenant les règles de transition
- Simulation textuelle et graphique des évolutions
- Exemples pratiques dans la **question 7**, où les fichiers suivants sont transformés en automates cellulaires puis simulés :
  - `automate_aⁿbⁿ`
  - `automate_cyclique`
  - `automate_symétrique`
  - `automate_croissance_infini`

### 🔹 Partie 2 – Machines de Turing

- Modélisation d’une machine de Turing
- Lecture des transitions à partir de fichiers
- Simulation de l’exécution sur une bande
- Détermination de l’acceptation ou du rejet d’un mot

### 🔹 Partie 3 – Simulation de MT avec AC

- Traduction d’une machine de Turing en automate cellulaire
- Vérification que les deux modèles donnent les mêmes résultats
- Étude du problème HALTING-CELLULAR-AUTOMATON (accompagnée d’un document PDF)

---

## 📦 Ce dont vous avez besoin

Aucune bibliothèque externe n’est nécessaire. Le projet fonctionne uniquement avec **Python 3**.

Pour que tout fonctionne correctement :
- Assurez-vous d’utiliser une version de Python récente (3.8 ou supérieure),
- Gardez l’organisation des dossiers intacte,
- Lancez les commandes depuis la racine du projet,
- Certains scripts ajoutent manuellement des chemins (`sys.path`) pour permettre les imports entre dossiers (utile pour la partie 3).

---

## 📚 Exemples de fichiers

- `Assets/exemple_MT.txt` : contient les transitions d’une machine de Turing
- `Assets/automate_cyclique.txt`, etc. : règles d’un automate cellulaire, utilisées dans les simulations graphiques

---

## ✍️ Auteurs

Projet réalisé par OURIMI Ayoub et LALMASSI Ilyan  dans le cadre du module **IN620 - Méta-simulation**, année universitaire 2024–2025.