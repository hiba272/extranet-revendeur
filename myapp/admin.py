from django.contrib import admin
from .models import Facture  # Importez le modèle Facture

class FactureAdmin(admin.ModelAdmin):
    readonly_fields = ('numero_facture',)
# Enregistrez le modèle Facture pour le rendre visible dans l'admin
admin.site.register(Facture, FactureAdmin)
