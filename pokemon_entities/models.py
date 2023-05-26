from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_en = models.CharField(max_length=20, verbose_name="Name in English")
    title_ru = models.CharField(
        max_length=20, verbose_name="Name in Russian", blank=True
    )
    title_jp = models.CharField(
        max_length=20, verbose_name="Name in Japanese", blank=True
    )
    description = models.TextField(verbose_name="Description", blank=True)
    image = models.ImageField(upload_to="", verbose_name="Image", blank=True)
    previous_evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.CASCADE,
        related_name="next_evolutions",
        verbose_name="Previous_evolution",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title_en


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name="Pokemon"
    )
    latitude = models.FloatField(max_length=50, verbose_name="Latitude")
    longitude = models.FloatField(max_length=50, verbose_name="Longitude")
    appeared_at = models.DateTimeField(
        verbose_name="Time and date of appearance", null=True, blank=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name="Time and date of disappearance", null=True, blank=True
    )
    level = models.IntegerField(verbose_name="Level", null=True, blank=True)
    health = models.IntegerField(verbose_name="Health", null=True, blank=True)
    strength = models.IntegerField(
        verbose_name="Strength", null=True, blank=True
    )
    defence = models.IntegerField(
        verbose_name="Defence", null=True, blank=True
    )
    stamina = models.IntegerField(
        verbose_name="Stamina", null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.pokemon.title_en} level {self.level}"
