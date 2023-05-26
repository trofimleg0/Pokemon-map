import folium
import urllib.parse

from .models import Pokemon, PokemonEntity
from django.utils import timezone
from django.shortcuts import render


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision"
    "/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832"
    "&fill=transparent"
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_time = timezone.localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemons_entities = PokemonEntity.objects.filter(
        appeared_at__lt=current_time, disappeared_at__gt=current_time
    )

    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url),
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        pokemons_on_page.append(
            {
                "pokemon_id": pokemon.id,
                "img_url": request.build_absolute_uri(pokemon.image.url),
                "title_en": pokemon.title_en,
            }
        )

    return render(
        request,
        "mainpage.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemons": pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):
    current_time = timezone.localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon = Pokemon.objects.get(id=pokemon_id)
    previous_evolution = {}
    next_evolution = {}

    if pokemon.previous_evolution:
        previous_evolution = {
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": request.build_absolute_uri(
                pokemon.previous_evolution.image.url
            ),
            "title_en": pokemon.previous_evolution.title_en,
        }

    for evolved_pokemon in pokemon.next_evolutions.all():
        next_evolution = {
            "pokemon_id": evolved_pokemon.id,
            "img_url": request.build_absolute_uri(evolved_pokemon.image.url),
            "title_en": evolved_pokemon.title_en,
        }

    pokemon_params = {
        "pokemon_id": pokemon.id,
        "img_url": request.build_absolute_uri(
            pokemon.image.url if pokemon.image else ""
        ),
        "title_en": pokemon.title_en,
        "title_ru": pokemon.title_ru,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "previous_evolution": previous_evolution,
        "next_evolution": next_evolution,
    }

    pokemons_entities = PokemonEntity.objects.filter(
        appeared_at__lt=current_time,
        disappeared_at__gt=current_time,
        pokemon__id__contains=pokemon_id,
    )

    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url),
        )

    return render(
        request,
        "pokemon.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemon": pokemon_params,
        },
    )
