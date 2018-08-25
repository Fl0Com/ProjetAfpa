from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Player(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player")
    avatar = models.ImageField("avatar", null=True, blank=True, upload_to="avatar/")
    dateNaissance = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Joueur"

def create_user_data(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)

post_save.connect(create_user_data, sender=User)