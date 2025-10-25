from django.db.models.signals import post_migrate, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User


@receiver(post_migrate)
def startup_message(sender, **kwargs):
    if settings.DEBUG:
        print("[Core] Migrações aplicadas com sucesso.")


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL] New user created: {instance.username}")
