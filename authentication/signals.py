from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    print('created:', created)
    if created:
        group, created = Group.objects.get_or_create(name="customer_user")
        print('created:', created)
        instance.groups.add(group)