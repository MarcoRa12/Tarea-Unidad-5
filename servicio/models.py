from django.db import models
from django.utils.translation import gettext_lazy as _
from usuario.models import createUser 
# Create your models here.

class Pagos(models.Model):
    class Servicios(models.TextChoices):
        Netflix = 'NF', _('Netflix')
        Amazon = 'AP', _('Amazon Video')
        Start = 'ST', _('Start+')
        Paramount = 'PM', _('Paramount+')

    servicio = models.CharField(
        max_length=2,
        choices=Servicios.choices,
        default=Servicios.Netflix,
    )
    fecha_pago = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(createUser, on_delete =models.CASCADE , null=True)
    monto = models.FloatField(default=0.0)