from django.db.models.signals import post_save
from django.dispatch import receiver
from newsroom_app.models import Field
from django.template import Template, Context


@receiver(post_save, sender=Field)
def generate_css(instance, **kwargs):
    pass