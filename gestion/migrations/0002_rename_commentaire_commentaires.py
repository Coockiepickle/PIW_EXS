# Generated by Django 5.0.3 on 2024-05-05 02:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commentaire',
            new_name='Commentaires',
        ),
    ]
