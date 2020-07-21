# Develop: vmgabriel

"""Define all Models for App GestionUsuario"""

from django.db import models

# All Models Here


class User(models.Model):
    """User Definition for the ORM and the Model"""
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    tfno = models.CharField(max_length=7, verbose_name='Phone')

    def __str__(self):
        return '{} - dir: {} - email: {} - phone: {}'.format(
            self.name,
            self.address,
            self.email,
            self.tfno
        )
