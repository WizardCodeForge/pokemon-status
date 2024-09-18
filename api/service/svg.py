from api.type.svg_service import SvgTheme
import requests
import base64


def get_svg_image(image: str) -> str:
    resp = requests.get(image)
    base64_str = base64.b64encode(resp.content).decode('utf-8')
    return f'<image href="data:image/png;base64,{base64_str}" x="150" height="200" width="140"/>'


def get_font(path: str) -> str:
    with open(path, "rb") as font_file:
        font_base64 = base64.b64encode(font_file.read()).decode('utf-8')
    return font_base64


def get_svg_progress(theme: SvgTheme, level: int, progress: int) -> str:
    return f'''
        <text x="200" y="185" class="pokemon-font truncate" fill="{theme["title"]}" text-anchor="middle" alignment-baseline="middle">Level {level}</text>
        <rect x="0" y="200" width="400" height="26" class="truncate" fill="{theme["background_bar"]}" stroke="#000000" stroke-width="2"/>
        <rect x="0" y="200" width="{progress}%" height="26" class="truncate" fill="{theme["gradient_init"]}" stroke="#000000" stroke-width="1"/>
        <rect x="0" y="200" width="{progress}%" height="26" class="truncate" fill="url(#grad1)" stroke="#000000" stroke-width="1"/>
        <text x="200" y="215" class="pokemon-font-small truncate" fill="#000000" text-anchor="middle" alignment-baseline="middle">{progress}%</text>
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:{theme["gradient_init"]};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{theme["gradient_final"]};stop-opacity:1" />
            </linearGradient>
        </defs>
    '''


def get_svg_configs(font) -> str:
    return f'''
        <style>
            @font-face {{
                font-family: 'Press Start 2P';
                src: url('data:font/ttf;base64,{font}') format('truetype');
            }}
            .pokemon-font {{
                font-family: 'Press Start 2P', cursive;
                font-size: 20px;
            }}
            .pokemon-font-small {{
                font-family: 'Press Start 2P', cursive;
                font-size: 18px;
            }}
            .truncate {{
                overflow: hidden;
                -o-text-overflow: ellipsis;
                text-overflow: ellipsis;
                white-space: nowrap;
            }}
        </style>
    '''


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

        case "ditto":
            colors["background_bar"] = "#FFFFFF"
            colors["gradient_init"] = "#DAD9E8"
            colors["gradient_final"] = "#B38CFF"
            colors["title"] = "#B38CFF"    

        case "sylveon":
            colors["background_bar"] = "#F0F0F0"
            colors["gradient_init"] = "#FF8CC5"
            colors["gradient_final"] = "#8CD4FF"
            colors["title"] = "#FF8CC5"    

        case "glaceon":
            colors["background_bar"] = "#E0F7FA"
            colors["gradient_init"] = "#74C2E1"
            colors["gradient_final"] = "#439297"
            colors["title"] = "#74C2E1"    

        case "marshadow":
            colors["background_bar"] = "#747577"
            colors["gradient_init"] = "#2C2E30"
            colors["gradient_final"] = "#E1DB87"
            colors["title"] = "#C25036"    

    return colors
