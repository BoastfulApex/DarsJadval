from django.db import models

INSTUTUT, NUKUS, SAMARQAND, FARGONA = (
    "Institut",
    "Nukus Filiali",
    "Samarqand filiali",
    "Farg'ona filali"
)


class StudyGroup(models.Model):
    FILIAL = (
        (INSTUTUT, INSTUTUT),
        (NUKUS, NUKUS),
        (SAMARQAND, SAMARQAND),
        (FARGONA, FARGONA)
    )

    name = models.CharField(max_length=1000, null=True, blank=True)
    weekly_schedule = models.FileField(null=True)
    filial = models.CharField(max_length=100, choices=FILIAL, null=True)

    @property
    def PhotoURL(self):
        try:
            return self.weekly_schedule.url
        except:
            return ''


class Teacher(models.Model):
    FILIAL = (
        (INSTUTUT, INSTUTUT),
        (NUKUS, NUKUS),
        (SAMARQAND, SAMARQAND),
        (FARGONA, FARGONA)
    )

    name = models.CharField(max_length=1000, null=True, blank=True)
    zoom_link = models.URLField(max_length=1000, null=True, blank=True)
    filial = models.CharField(max_length=100, choices=FILIAL, null=True)
