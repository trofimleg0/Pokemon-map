from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=20, verbose_name="Имя на русском")
    title_en = models.CharField(
        max_length=20, verbose_name="Имя на английском", blank=True
    )
    title_jp = models.CharField(
        max_length=20, verbose_name="Имя на японском", blank=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(
        upload_to="", verbose_name="Изображение", blank=True
    )
    previous_evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.CASCADE,
        related_name="next_evolutions",
        verbose_name="Предыдущая эволюция",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name="Покемон"
    )
    latitude = models.FloatField(max_length=50, verbose_name="Ширина")
    longitude = models.FloatField(max_length=50, verbose_name="Долгота")
    appeared_at = models.DateTimeField(
        verbose_name="Время и дата появления", null=True, blank=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name="Время и дата исчезновения", null=True, blank=True
    )
    level = models.IntegerField(verbose_name="Уровень", null=True, blank=True)
    health = models.IntegerField(
        verbose_name="Здоровье", null=True, blank=True
    )
    strength = models.IntegerField(verbose_name="Сила", null=True, blank=True)
    defence = models.IntegerField(
        verbose_name="Защита", null=True, blank=True
    )
    stamina = models.IntegerField(
        verbose_name="Выносливость", null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.pokemon.title_ru} level {self.level}"
