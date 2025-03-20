# app/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
import json

from .forms import IrisPredictionForm, IrisSpeciesForm
from .models import IrisFeature
from .ml_model import IrisModel

# Créer une instance du modèle
iris_model = IrisModel()

class HomeView(View):
    def get(self, request):
        prediction_form = IrisPredictionForm()
        species_form = IrisSpeciesForm()
        
        # S'assurer que les données sont correctement formatées pour JSON
        species_info = iris_model.get_species_info()
        
        # Convertir des types numpy en types Python standard pour la sérialisation JSON
        for species in species_info.values():
            for key, value in species['avg_characteristics'].items():
                species['avg_characteristics'][key] = float(value)
            for key, value in species['min_characteristics'].items():
                species['min_characteristics'][key] = float(value)
            for key, value in species['max_characteristics'].items():
                species['max_characteristics'][key] = float(value)
        
        context = {
            'prediction_form': prediction_form,
            'species_form': species_form,
            'species_info': json.dumps(species_info),  # Convertir en JSON
        }
        return render(request, 'home.html', context)

class PredictView(View):
    def post(self, request):
        form = IrisPredictionForm(request.POST)
        
        if form.is_valid():
            features = [
                form.cleaned_data['sepal_length'],
                form.cleaned_data['sepal_width'],
                form.cleaned_data['petal_length'],
                form.cleaned_data['petal_width']
            ]
            
            predicted_species = iris_model.predict(features)
            species_info = iris_model.get_species_info()[predicted_species]
            
            # Convertir des types numpy en types Python standard
            for key, value in species_info['avg_characteristics'].items():
                species_info['avg_characteristics'][key] = float(value)
            for key, value in species_info['min_characteristics'].items():
                species_info['min_characteristics'][key] = float(value)
            for key, value in species_info['max_characteristics'].items():
                species_info['max_characteristics'][key] = float(value)
                
            iris_feature = form.save(commit=False)
            iris_feature.species = predicted_species
            iris_feature.save()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'species': predicted_species,
                    'species_info': species_info,
                })
            
            messages.success(request, f"Prédiction: Iris {predicted_species.capitalize()}")
            return redirect('home')
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors,
            })
        
        return redirect('home')

class SpeciesInfoView(View):
    def post(self, request):
        form = IrisSpeciesForm(request.POST)
        
        if form.is_valid():
            species_name = form.cleaned_data['species']
            species_info = iris_model.get_species_info()[species_name]
            
            # Convertir des types numpy en types Python standard
            for key, value in species_info['avg_characteristics'].items():
                species_info['avg_characteristics'][key] = float(value)
            for key, value in species_info['min_characteristics'].items():
                species_info['min_characteristics'][key] = float(value)
            for key, value in species_info['max_characteristics'].items():
                species_info['max_characteristics'][key] = float(value)
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'species_info': species_info,
                })
            
            return redirect('home')
            
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors,
            })
            
        return redirect('home')