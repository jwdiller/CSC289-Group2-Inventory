from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django import template

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
register = template.Library()

@register.simple_tag(takes_context=True)
def cssTheme(context):
    user = context['user']
    try:
        profile = Profile.objects.get(user=user)
        return profile.cssTheme
    except Profile.DoesNotExist:
        return 'default'