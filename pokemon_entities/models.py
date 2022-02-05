from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, null=True, verbose_name='Название по-русски')
    title_en = models.CharField(max_length=200, null=True, verbose_name='Название по-английски')
    title_jp = models.CharField(max_length=200, null=True, verbose_name='Название по-японски')
    image = models.ImageField(upload_to='pokemons', blank=True, null=True, verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return '{}'.format(self.title_ru)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_entities')
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(default=50, null=True, blank=True)
    health = models.IntegerField(default=50, null=True, blank=True)
    strength = models.IntegerField(default=50, null=True, blank=True)
    defense = models.IntegerField(default=50, null=True, blank=True)
    stamina = models.IntegerField(default=50, null=True, blank=True)
