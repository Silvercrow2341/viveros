from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import profile

@receiver(post_save, sender=profile)
def add_user_to_guest_group(sender, instance, created, **kwargs):
    if created:
        try:
            guest = Group.objects.get(name='usuario')

        except Group.DoesNotExist:
            guest = Group.objects.create(name='usuario')



        instance.user.groups.add(guest)