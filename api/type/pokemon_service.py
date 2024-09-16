from typing import TypedDict


class PrimaryDTO(TypedDict):
    evolution_url: str
    growth_url: str


class PokemonDTO(TypedDict):
    name: str
    gif: str
    level: int
    initial_level_xp: int
    current_level_xp: int
    finally_level_xp: int
