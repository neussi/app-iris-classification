from django.db import models

class IrisFeature(models.Model):
    sepal_length = models.FloatField(verbose_name="Longueur du sépale (cm)")
    sepal_width = models.FloatField(verbose_name="Largeur du sépale (cm)")
    petal_length = models.FloatField(verbose_name="Longueur du pétale (cm)")
    petal_width = models.FloatField(verbose_name="Largeur du pétale (cm)")
    
    SPECIES_CHOICES = [
        ('setosa', 'Iris setosa'),
        ('versicolor', 'Iris versicolor'),
        ('virginica', 'Iris virginica'),
    ]
    
    species = models.CharField(
        max_length=20,
        choices=SPECIES_CHOICES,
        blank=True,
        null=True,
        verbose_name="Espèce"
    )
    
    prediction_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de prédiction")
    
    def __str__(self):
        return f"Iris {self.species if self.species else 'non classifié'}"