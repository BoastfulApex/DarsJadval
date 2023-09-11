from django.contrib import admin
from .models import *


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    fields = []


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = []

