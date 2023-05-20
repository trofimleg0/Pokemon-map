# Pokemon Map

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)

### Description

Website for help on the [Pokemon GO](https://www.pokemongo.com/en-us/). This is a game about catching [Pokemons](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).

The essence of the game is that Pokemon periodically appear on the map, for a certain period of time. Each player can catch a Pokemon for himself, and replenish his personal collection.

There may be several individuals of the same Pokemon on the map at once: for example, 3 Bulbasaurs. Each individual can be caught by several players at once. If a player catches a Pokemon, it disappears for him, but remains for others.

The game has evolution mechanics. Pokemon of one kind can "evolve" into another. So, for example, a Bulbasaurus turns into an Ivisaurus, and that turns into a Venusaurus.

![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/)

### How to launch

To run the site, you will need Python third version(Recommend 3.8.16).

Download the code from GitHub. Then install the dependencies

```sh
pip install -r requirements.txt
```

Run the development server

```sh
python3 manage.py runserver
```

### Environment variables

Some of the project settings are taken from the environment variables. To identify them, create a `.env` file next to `manage.py ` and write the data there in this format: `VARIABLE=value'.

2 variables are available:
- `DEBUG` — debug mode. Set True to see debugging information in case of an error.
- `SECRET_KEY` — the secret key of the project

## Project goals

The code is written for educational purposes — this is a lesson in a course on Python and web development on the Devman.
