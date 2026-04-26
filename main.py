"""import pandas as pd

# ÉTAPE 1 : Génération du fichier ventes.csv 
data = {
    'ID': [101, 102, 103],
    'Prix': [15.0, 25.0, 10.0],
    'Quantite': [3, 2, 5],
    'Remise': [10, 5, 0] 
}
df = pd.DataFrame(data)
df.to_csv('ventes.csv', index=False)
print("Étape 1 : Fichier ventes.csv généré.")"""
import pandas as pd
import random

# On prépare 3000 lignes de données
lignes = []

for i in range(1, 3001):
    lignes.append({
        'ID': 1000 + i,                   # IDs de 1001 à 4000
        'Prix': round(random.uniform(5.0, 500.0), 2),  # Prix entre 5 et 500 DT
        'Quantite': random.randint(1, 50),             # Quantité entre 1 et 50
        'Remise': random.choice([0, 5, 10, 15, 20, 30]) # Remises variées
    })
    # Création du fichier ventes.csv avec l'en-tête [cite: 12]
df = pd.DataFrame(lignes)
df.to_csv('ventes.csv', index=False)

print(f"Succès ! Le fichier 'ventes.csv' contient maintenant {len(df)} lignes.")


# ÉTAPE 2 : Calcul du CA Brut 
df['CA_Brut'] = df['Prix'] * df['Quantite'] 

# ÉTAPE 3 : CA Net 
# On applique la remise 
df['CA_Net'] = df['CA_Brut'] * (1 - df['Remise'] / 100) 

# ÉTAPE 4 : On calcule la TVA de 20% sur le CA Net
df['TVA'] = df['CA_Net'] * 0.20 

# ÉTAPE 5 : Affichage 
print(df)

# ÉTAPE 6 : Identifier le produit le plus rentable 
# On cherche la ligne où le CA_Net est le plus élevé
index_du_meilleur = df['CA_Net'].idxmax() 

# On récupère l'ID correspondant à cet index
id_produit_star = df.loc[index_du_meilleur, 'ID']

# Affichage du résultat
print("-" * 30)
print(f"ANALYSE DE PERFORMANCE :")
print(f"Le produit le plus rentable est l'ID : {id_produit_star}")
print("-" * 30)

# ÉTAPE 7 : Exportation finale
# Cette commande crée le fichier avec TOUTES les colonnes (anciennes et nouvelles)
df.to_csv('resultats_final.csv', index=False)

print("Succès : Le fichier 'resultats_final.csv' a été mis à jour avec toutes les colonnes.")
import matplotlib.pyplot as plt

# ÉTAPE 8: Graphique 

# 1. Création du graphique (Barres)
# On met l'ID en bas (x) et le CA_Net en hauteur (y)
plt.bar(df['ID'].astype(str), df['CA_Net'], color='skyblue', label='CA Net par produit')
plt.axhline(df['CA_Net'].mean(), color='red', linestyle='--', label='Moyenne') # Ligne de moyenne
plt.legend() # Affiche la légende
plt.title('Performance des Ventes')
plt.show()

# 3. Affichage du graphique
plt.show()
# Un petit résumé statistique pour le rapport
print("Résumé statistique des ventes :")
print(df.describe())

#  Lecture dynamique 
try:
    # On lit le fichier qui existe déjà dans le dossier
    df = pd.read_csv('ventes.csv')
    print(f"Succès : Le fichier a été lu. Nombre de lignes détectées : {len(df)}")
except FileNotFoundError:
    print("Erreur : Le fichier 'ventes.csv' est introuvable !")



