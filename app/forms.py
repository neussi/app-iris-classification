from django import forms
from .models import IrisFeature

class IrisPredictionForm(forms.ModelForm):
    class Meta:
        model = IrisFeature
        fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['step'] = 0.1

class IrisSpeciesForm(forms.Form):
    species = forms.ChoiceField(
        choices=IrisFeature.SPECIES_CHOICES,
        label="Espèce d'Iris",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )