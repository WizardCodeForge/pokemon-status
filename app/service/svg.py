from type.pokemon_service import PokemonDTO
from type.svg_service import SvgTheme


def get_svg_image(image: str) -> str:
    return f'<image href="{image}" width="200" height="200" x="100" y="10" />'


def get_svg_progress(theme: SvgTheme, pokemon: PokemonDTO, progress: int) -> str:
    return f'''
        <rect x="50" y="225" width="200" height="10" fill="{theme["background_bar"]}" rx="8" />
        <rect x="50" y="225" width="{progress}" height="10" fill="{theme["progress_bar"]}" rx="8" />
        <text x="150" y="250" font-size="7" text-anchor="middle" fill="{theme["xp"]}">{pokemon['current_level_xp']}</text>
        <text x="50" y="250" font-size="7" text-anchor="middle" fill="{theme["xp"]}">{pokemon['initial_level_xp']}</text>
        <text x="250" y="250" font-size="7" text-anchor="middle" fill="{theme["xp"]}">{pokemon["finally_level_xp"]}</text>
        <text x="150" y="290" font-size="15" text-anchor="middle" font-weight="bold" fill="{theme["title"]}">Level {pokemon["level"]}</text>
    '''


def get_theme(theme: str) -> SvgTheme:
    print(theme)

    colors: SvgTheme = {}

    match theme:
        case "charmander":
            colors["background_bar"] = "Cornsilk"
            colors["progress_bar"] = "DarkOrange"
            colors["title"] = "DarkOrange"
            colors["xp"] = "Coral"

        case "pikachu":
            colors["background_bar"] = "LightYellow"
            colors["progress_bar"] = "Gold"
            colors["title"] = "Tomato"
            colors["xp"] = "Tomato"

        case "dratini":
            colors["background_bar"] = "LightCyan"
            colors["progress_bar"] = "SteelBlue"
            colors["title"] = "RoyalBlue"
            colors["xp"] = "MediumSlateBlue"

        case "bulbasaur":
            colors["background_bar"] = "PaleGreen"
            colors["progress_bar"] = "DarkGreen"
            colors["title"] = "MediumSeaGreen"
            colors["xp"] = "MediumTurquoise"

        case _:
            colors["background_bar"] = "Pink"
            colors["progress_bar"] = "DeepPink"
            colors["title"] = "PaleVioletRed"
            colors["xp"] = "PaleVioletRed"

    return colors
