# Generated by Django 4.2 on 2023-09-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('weekly_schedule', models.FileField(null=True, upload_to='')),
                ('filial', models.CharField(choices=[('Institut', 'Institut'), ('Nukus Filiali', 'Nukus Filiali'), ('Samarqand filiali', 'Samarqand filiali'), ("Farg'ona filali", "Farg'ona filali")], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('zoom_link', models.URLField(blank=True, max_length=1000, null=True)),
                ('filial', models.CharField(choices=[('Institut', 'Institut'), ('Nukus Filiali', 'Nukus Filiali'), ('Samarqand filiali', 'Samarqand filiali'), ("Farg'ona filali", "Farg'ona filali")], max_length=1000, null=True)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]
