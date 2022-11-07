import datetime

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Experiment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    experiment_number = models.CharField(max_length=20)
    experiment_date = models.DateField(auto_now_add=True)
    sample_name = models.CharField(max_length=20)
    powder_comp = models.CharField(max_length=20)
    synthesis_method = models.CharField(max_length=20)
    polymer = models.CharField(max_length=20)
    substrate = models.CharField(max_length=20)
    deposition = models.CharField(max_length=20)
    nanoparticle_percentage = models.IntegerField()
    polymer_percentage = models.IntegerField()
    linker_composite = models.CharField(max_length=20)
    linker_percentage = models.IntegerField()
    geometry = models.CharField(max_length=20)
    thickness = models.IntegerField()
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.experiment_number)


class Record(models.Model):
    experiment_id = models.ForeignKey(Experiment, related_name="records", on_delete=models.CASCADE)
    measurement_order = models.IntegerField()
    resistance = models.FloatField()
    voltage = models.FloatField()
    temp = models.FloatField()

    class Meta:
        unique_together = ['experiment_id', 'measurement_order']
        ordering = ['measurement_order']

    def __str__(self):
        return str(self.experiment_id) + '|' + str(self.measurement_order)
