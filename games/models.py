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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # auto_increment_id = models.AutoField(primary_key=True, verbose_name = 'id')
    # pseudo = models.CharField(max_length=100, verbose_name= 'pseudo', unique=True)
    gender = models.CharField(max_length=20, verbose_name= 'civilité', choices=GENDER_CHOICES )
    avatar = models.ImageField("avatar", null=True, blank=True, upload_to="avatar/")
    dateNaissance = models.DateField(null=True)


    def __str__(self):
        return self.pseudo

    class Meta:
        verbose_name = "Joueur"