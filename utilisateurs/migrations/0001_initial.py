# Generated by Django 5.0.3 on 2024-05-05 02:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('noRestaurant', models.AutoField(primary_key=True, serialize=False)),
                ('nomRestaurant', models.CharField(max_length=25)),
                ('villeRestaurant', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TypeResto',
            fields=[
                ('noType', models.AutoField(primary_key=True, serialize=False)),
                ('nomType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('noCommentaire', models.AutoField(primary_key=True, serialize=False)),
                ('commentaire', models.TextField()),
                ('note', models.IntegerField(default=0)),
                ('dateCommentaire', models.DateField(auto_now_add=True)),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('noRestaurant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='utilisateurs.restaurants')),
            ],
        ),
        migrations.AddField(
            model_name='restaurants',
            name='typeRestaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='utilisateurs.typeresto'),
        ),
    ]
