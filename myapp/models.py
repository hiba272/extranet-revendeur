from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid
class Facture(models.Model):

    tel_adsl_client = models.CharField(max_length=20)
    identifiant = models.CharField(max_length=50, blank=True, null=True)  # Ajoutez ce champ si nécessaire
    abonnement = models.CharField(max_length=100, blank=True, null=True)  # Ajoutez ce champ si nécessaire
    mois = models.CharField(max_length=20)
    annee = models.IntegerField()
    numero_facture = models.CharField(max_length=20, unique=True, blank=True)
    date_creation = models.DateTimeField()
    date_fin_paiement = models.DateTimeField()
    montant_facture = models.DecimalField(max_digits=10, decimal_places=3)
    date_debut_facture = models.DateTimeField()
    date_fin_facture = models.DateTimeField()
    proprietaire_cheque = models.CharField(max_length=100, blank=True, null=True)  # Nouveau champ pour le propriétaire du chèque
    def __str__(self):
        return f"{self.numero_facture} - {self.tel_adsl_client}"
    # Signal pour générer automatiquement un numéro de facture
@receiver(pre_save, sender=Facture)
def generate_facture_number(sender, instance, **kwargs):
    if not instance.numero_facture:
        instance.numero_facture = str(uuid.uuid4()).split('-')[0].upper()  # Génère un numéro unique