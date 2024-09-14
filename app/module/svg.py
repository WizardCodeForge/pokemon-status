from service.svg import get_svg_image, get_svg_progress, get_theme
from type.pokemon_service import PokemonDTO


def get_svg_banner(pokemon: PokemonDTO, theme: str) -> str:
    themeColors = get_theme(theme)

    percent = (pokemon["current_level_xp"] / pokemon["finally_level_xp"]) * 100
    progressFill = 100 + percent

    progress = get_svg_progress(themeColors, pokemon, progressFill)

    image = get_svg_image(pokemon['gif'])

    return f'''
        <svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" style="font-family:Roboto-Regular,Roboto">
            {image}
            {progress}
        </svg>
        '''
