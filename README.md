# Projet de Fin d'Année : Automatisation des Ventes
## Description
**Ce projet Python a été réalisé dans le cadre de l'unité de matière Logiciels à la Faculté des Sciences de Tunis. L'objectif est d'automatiser l'analyse des données de ventes d'une entreprise de e-commerce qui utilisait auparavant des tableurs Excel limités par le volume de données**

## Fonctionnalités
**Le script Python réalise les actions suivantes :**
### **Génération de données :**

Création automatique d'un fichier ventes.csv avec les colonnes ID, Prix, Quantité et Remise.

#### **Calculs financiers :**

* Calcul du Chiffre d'Affaires (CA) Brut.

* Application des remises en pourcentage pour obtenir le CA Net.
 * Calcul de la TVA (20%) sur le CA Net.

### **Analyse de performance :**
 * Affichage du CA Total de l'entreprise.
 * Identification du produit (ID) ayant généré le plus gros bénéfice.

### **Exportation :** 
 Sauvegarde de toutes les colonnes originales et calculées dans un fichier resultats_final.csv 

## Prérequis
* Langage : Python
* Environnement : VS Code 
* Bibliothèques :
         Pandas (Manipulation de données)
         Matplotlib (Visualisation)
## Installation
* python -m venv .venv 
 * pip install pandas matplotlib
## Utilisation
 * python main.py
## Auteurs 
* mariem aouichi
* mariem ben hessine
* asma hafien

