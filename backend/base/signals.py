from django.db.models.signals import pre_save
from django.contrib.auth.models import User


def upadteUser(sender, instance, **kwargs):
    print('Signal triggered', instance.email)
    user = instance
    if user.email != '':
        user.username = user.email


pre_save.connect(upadteUser, sender=User)
