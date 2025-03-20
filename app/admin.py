# iris_app/admin.py

from django.contrib import admin
from .models import IrisFeature

@admin.register(IrisFeature)
class IrisFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'species', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'prediction_date')
    list_filter = ('species', 'prediction_date')
    search_fields = ('species',)
    date_hierarchy = 'prediction_date'
    readonly_fields = ('prediction_date',)
    fieldsets = (
        ("Caractéristiques", {
            'fields': ('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
        }),
        ("Résultat", {
            'fields': ('species', 'prediction_date')
        }),
    )