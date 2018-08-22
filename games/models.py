from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Player(models.Model):
    MONSIEUR = "Mr."
    MADAME = "Mme"
    GENDER_CHOICES = (
        ( MONSIEUR, 'Monsieur'),
        ( MADAME, 'Madame'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player")

    gender = models.CharField(max_length=20, verbose_name= 'civilité', choices=GENDER_CHOICES )
    avatar = models.ImageField("avatar", null=True, blank=True, upload_to="avatar/")
    dateNaissance = models.DateField(null=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Joueur"