.PHONY: all partie1 partie2 partie3
all: partie1 partie2 partie3

partie1:
	@echo "===================="
	@echo "      PARTIE 1      "
	@echo "===================="
	@echo "----- Question 1 : Automate_Cellulaire -----"
	python Partie1/A_AutomateCellulaire.py
	@echo "----- Question 2 : Configuration -----"
	python Partie1/B_Configuration.py
	@echo "----- Question 3 : Lecture Fichier Automate -----"
	python Partie1/C_Lecture_Fichier_Automate.py
	@echo "----- Question 4 : Configuration Suivante -----"
	python Partie1/D_Config_Suivante.py
	@echo "----- Question 5 : Simulation -----"
	python Partie1/E_Simulation.py
	@echo "----- Question 6 : Simulation Graphique -----"
	python Partie1/F_Simulation_Graphique.py
	@echo "----- Question 7 : Automate Cellulaire Graphique -----"
	python Partie1/G_Exemples_Automates.py

partie2:
	@echo "===================="
	@echo "      PARTIE 2      "
	@echo "===================="
	@echo "----- Question 8 : Machine de Turing -----"
	python Partie2/A_MachineTuring.py
	@echo "----- Question 9 : Configuration MT -----"
	python Partie2/B_MTConfiguration.py
	@echo "----- Question 10 : Lecture Fichier MT -----"
	python Partie2/C_Lecture_Fichier_MT.py
	@echo "----- Question 11 : Configuration Suivante MT -----"
	python Partie2/D_MTConfig_Suivante.py
	@echo "----- Question 12 : Simulation MT -----"
	python Partie2/E_MTSimulation.py

partie3:
	@echo "===================="
	@echo "      PARTIE 3      "
	@echo "===================="
	@echo "----- Question 13 : Automate Cellulaire depuis une MT -----"
	python Partie3/A_AutomateC_Depuis_MT.py

q1:
	@echo "----- Question 1 : Automate_Cellulaire -----"
	python Partie1/A_AutomateCellulaire.py

q2:
	@echo "----- Question 2 : Configuration -----"
	python Partie1/B_Configuration.py
q3:
	@echo "----- Question 3 : Lecture Fichier Automate -----"
	python Partie1/C_Lecture_Fichier_Automate.py
q4:
	@echo "----- Question 4 : Configuration Suivante -----"
	python Partie1/D_Config_Suivante.py
q5:
	@echo "----- Question 5 : Simulation -----"
	python Partie1/E_Simulation.py
q6:
	@echo "----- Question 6 : Simulation Graphique -----"
	python Partie1/F_Simulation_Graphique.py
q7:
	@echo "----- Question 7 : Automate Cellulaire Graphique -----"
	python Partie1/G_Exemples_Automates.py
q8:
	@echo "----- Question 8 : Machine de Turing -----"
	python Partie2/A_MachineTuring.py
q9:
	@echo "----- Question 9 : Configuration MT -----"
	python Partie2/B_MTConfiguration.py
q10:
	@echo "----- Question 10 : Lecture Fichier MT -----"
	python Partie2/C_Lecture_Fichier_MT.py
q11:
	@echo "----- Question 11 : Configuration Suivante MT -----"
	python Partie2/D_MTConfig_Suivante.py
q12:
	@echo "----- Question 12 : Simulation MT -----"
	python Partie2/E_MTSimulation.py
q13:
	@echo "----- Question 13 : Automate Cellulaire depuis une MT -----"
	python Partie3/A_AutomateC_Depuis_MT.py