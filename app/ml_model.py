import os
import pickle
import numpy as np
from sklearn import datasets

class IrisModel:
    def __init__(self):
        # Chemin vers le modèle
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.model_path = os.path.join(base_dir, 'data', 'iris_model_bin.pickle')
        
        # Charger le dataset Iris pour les statistiques
        self.iris_dataset = datasets.load_iris()
        
        # Mapping des indices vers les noms d'espèces
        self.species_mapping = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }
        
        # Noms des caractéristiques
        self.feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        
        # Charger le modèle
        try:
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            print(f"Modèle chargé depuis {self.model_path}")
        except Exception as e:
            print(f"Erreur lors du chargement du modèle: {e}")
            self.model = None
    
    def predict(self, features):
        """Prédit l'espèce d'iris à partir des caractéristiques"""
        if self.model is None:
            return 'setosa'  # Fallback par défaut
        
        # Convertir les features en array numpy
        X = np.array([features])
        
        try:
            # Faire la prédiction
            prediction = int(self.model.predict(X)[0])
            return self.species_mapping.get(prediction, 'setosa')
        except Exception as e:
            print(f"Erreur de prédiction: {e}")
            return 'setosa'  # Fallback par défaut
    
    def get_species_info(self):
        """Retourne les statistiques pour chaque espèce"""
        species_info = {}
        
        for idx, species_name in self.species_mapping.items():
            # Filtrer les données pour cette espèce
            species_data = self.iris_dataset.data[self.iris_dataset.target == idx]
            
            # Calculer les statistiques
            info = {
                'name': species_name,
                'display_name': f"Iris {species_name.capitalize()}",
                'count': len(species_data),
                'avg_characteristics': dict(zip(self.feature_names, species_data.mean(axis=0))),
                'min_characteristics': dict(zip(self.feature_names, species_data.min(axis=0))),
                'max_characteristics': dict(zip(self.feature_names, species_data.max(axis=0))),
            }
            
            species_info[species_name] = info
        
        return species_info