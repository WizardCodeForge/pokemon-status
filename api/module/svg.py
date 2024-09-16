from app.service.svg import get_svg_image, get_svg_progress, get_theme, get_svg_configs
from app.type.pokemon_service import PokemonDTO
import math


def get_svg_banner(pokemon: PokemonDTO, theme: str) -> str:
    percent = (pokemon["current_level_xp"] - pokemon["initial_level_xp"]) / (pokemon["finally_level_xp"] - pokemon["initial_level_xp"]) * 100
    percent = math.ceil(percent)

    themeColors = get_theme(theme)
    progress = get_svg_progress(themeColors, pokemon["level"], percent)
    config = get_svg_configs()
    image = get_svg_image(pokemon['gif'])

    return f'''
        <svg width="400" height="270" xmlns="http://www.w3.org/2000/svg">
            {config}
            {image}
            {progress}
        </svg>
        '''
