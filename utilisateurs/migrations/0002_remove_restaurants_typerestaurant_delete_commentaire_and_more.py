# Generated by Django 5.0.3 on 2024-05-05 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurants',
            name='typeRestaurant',
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
        migrations.DeleteModel(
            name='Restaurants',
        ),
        migrations.DeleteModel(
            name='TypeResto',
        ),
    ]
