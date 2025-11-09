from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Nombre', max_length=100, blank=True)
    last_name = models.CharField('Apellido', max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField('Biografía', blank=True)
    birthday = models.DateField('Fecha de nacimiento', null=True, blank=True)
    website = models.URLField('Sitio web', blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        # Si existe profile, guardarlo (evita fallos si ya existe)
        if hasattr(instance, 'profile'):
            instance.profile.save()
