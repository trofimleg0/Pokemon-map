# Generated by Django 3.1.14 on 2023-05-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_entities", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="defence",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="health",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="level",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="stamina",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="strength",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
