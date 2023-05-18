from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=50)
    longitude = models.FloatField(max_length=50)
    appeared_at = models.DateTimeField(blank=True)
    disappeared_at = models.DateTimeField(blank=True)
    level = models.IntegerField(default=1, blank=True)
    health = models.IntegerField(blank=True)
    strength = models.IntegerField(blank=True)
    defence = models.IntegerField(blank=True)
    stamina = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return f'{self.pokemon.title} {self.level}'
