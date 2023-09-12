from django.db import models
from django.contrib.auth.models import AbstractUser

INSTUTUT, NUKUS, SAMARQAND, FARGONA = (
    "Institut",
    "Nukus Filiali",
    "Samarqand filiali",
    "Farg'ona filali"
)


class User(AbstractUser):
    FILIAL = (
        (INSTUTUT, INSTUTUT),
        (NUKUS, NUKUS),
        (SAMARQAND, SAMARQAND),
        (FARGONA, FARGONA)
    )
    filial = models.CharField(max_length=100, choices=FILIAL, null=True)

