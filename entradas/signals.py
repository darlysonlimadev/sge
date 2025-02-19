from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from entradas.models import Entrada

@receiver(post_save, sender=Entrada)
def update_produto_quantidade(sender, instance, created, **kwargs):
    if created and instance.quantidade > 0:
        instance.produto.quantidade = F('quantidade') + instance.quantidade
        instance.produto.save()
