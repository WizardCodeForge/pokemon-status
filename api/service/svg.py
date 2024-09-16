from api.type.svg_service import SvgTheme


def get_svg_image(image: str) -> str:
        return f'''
        <svg width="200" height="140" xmlns="http://www.w3.org/2000/svg">
            <image href="{image}" x="0" y="0" width="200" height="140" />
        </svg>
    '''


def get_svg_progress(theme: SvgTheme, level: int, progress: int) -> str:
    return f'''
        <text x="200" y="170" class="pokemon-font" fill="{theme["title"]}" text-anchor="middle" alignment-baseline="middle">Level {level}</text>
        <rect x="0" y="200" width="400" height="26" fill="{theme["background_bar"]}" stroke="#000000" stroke-width="2"/>
        <rect x="0" y="200" width="{progress}%" height="26" fill="{theme["gradient_init"]}" stroke="#000000" stroke-width="1"/>
        <rect x="0" y="200" width="{progress}%" height="26" fill="url(#grad1)" stroke="#000000" stroke-width="1"/>
        <text x="200" y="215" class="pokemon-font-small" fill="#000000" text-anchor="middle" alignment-baseline="middle">{progress}%</text>
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:{theme["gradient_init"]};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{theme["gradient_final"]};stop-opacity:1" />
            </linearGradient>
        </defs>
    '''


def get_svg_configs() -> str:
    return """
    <style>
        .pokemon-font {
        font-family: 'Press Start 2P', cursive;
        font-size: 20px;
        }
        .pokemon-font-small {
        font-family: 'Press Start 2P', cursive;
        font-size: 18px;
        }
    </style>
    <defs>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P');
        </style>
    </defs>
    """


def get_theme(theme: str) -> SvgTheme:
    colors: SvgTheme = {}

    match theme:
        case "charmander":
            colors["background_bar"] = "#FFF8DC"
            colors["gradient_init"] = "#FFA500"
            colors["gradient_final"] = "#DC143C"
            colors["title"] = "#FF6347"

        case "pikachu":
            colors["background_bar"] = "#FFFFE0"
            colors["gradient_init"] = "#F0E68C"
            colors["gradient_final"] = "#FFD700"
            colors["title"] = "#FFD700"

        case "dratini":
            colors["background_bar"] = "#E0FFFF"
            colors["gradient_init"] = "#00FFFF"
            colors["gradient_final"] = "#4682B4"
            colors["title"] = "#4682B4"

        case "bulbasaur":
            colors["background_bar"] = "#E0FFFF"
            colors["gradient_init"] = "#00FFFF"
            colors["gradient_final"] = "#228B22"
            colors["title"] = "#228B22"

    return colors
