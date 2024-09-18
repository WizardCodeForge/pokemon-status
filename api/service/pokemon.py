import requests
from api.type.pokemon_service import PrimaryDTO


def get_primary_infos(pokemon: str) -> tuple[PrimaryDTO, bool]:
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}"

    try:
        res = requests.get(url)
        data = res.json()

        values: PrimaryDTO = {
            "evolution_url": data["evolution_chain"]["url"],
            "growth_url": data["growth_rate"]["url"]
        }
        validation: bool = True

    except Exception:
        values: PrimaryDTO = {
            "evolution_url": "",
            "growth_url": ""
        }
        validation: bool = False

    finally:
        return values, validation


def get_level(growth_url: str, xp: int) -> tuple[int, int, int]:
    res = requests.get(growth_url)
    data = res.json()

    for i, segment in enumerate(data["levels"]):
        if xp < segment["experience"]:
            level: int = data["levels"][i-1]["level"]
            finish_ex: int = segment["experience"]
            initial_xp: int = data["levels"][i-1]["experience"]

            return level, initial_xp, finish_ex

    else:
        level: int = 100
        finish_ex: int = xp
        initial_xp: int = data["levels"][-1]["experience"]

        return level, initial_xp, finish_ex


def get_pokemon_by_level(evolution_url: str, level: int) -> str:
    res = requests.get(evolution_url)
    data = res.json()

    current_pokemon = data["chain"]
    if current_pokemon["is_baby"]:
        current_pokemon = current_pokemon["evolves_to"][0]

    current_name = current_pokemon["species"]["name"]
    print(current_name)

    if not current_pokemon["evolves_to"]:
        return current_name

    while current_pokemon["evolves_to"]:
        evolution_details = current_pokemon["evolves_to"][0]["evolution_details"]

        if evolution_details[0]["trigger"]["name"] == "level-up":
            if evolution_details and "min_level" in evolution_details[0]:
                min_level = evolution_details[0]["min_level"]

                if level < min_level:
                    return current_name

                current_name = current_pokemon["evolves_to"][0]["species"]["name"]

            current_pokemon = current_pokemon["evolves_to"][0]

        # TODO adaptar evolucoes por item...
        else:
            current_pokemon = current_pokemon["evolves_to"][0]

    return current_name


def get_pokemon_gif(name: str) -> str:
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    res = requests.get(url)
    data = res.json()

    gif = data["sprites"]["versions"]["generation-v"]["black-white"]["animated"]["front_default"]

    return gif
