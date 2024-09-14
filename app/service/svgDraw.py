from type.pokemon_service import PokemonDTO


def get_svg_draw(p: PokemonDTO):
    image = f'<image href="{p["gif"]}" width="200" height="200" x="100" y="10" />'

    percent = (p["current_level_xp"] / p["finally_level_xp"]) * 100
    progressFill = 100 + percent

    progressBar = f'''
        <rect x="50" y="225" width="200" height="10" fill="lightgray" rx="8" />
        <rect x="50" y="225" width="{progressFill}" height="10" fill="Turquoise" rx="8" />
        <text x="150" y="250" font-size="7" text-anchor="middle" fill="DarkCyan">{p['current_level_xp']}</text>
        <text x="50" y="250" font-size="7" text-anchor="middle" fill="DarkCyan">{p['initial_level_xp']}</text>
        <text x="250" y="250" font-size="7" text-anchor="middle" fill="DarkCyan">{p["finally_level_xp"]}</text>
        <text x="150" y="290" font-size="15" text-anchor="middle" fill="Turquoise">Level {p["level"]}</text>
    '''

    return f'''
        <svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" style="font-family:Roboto-Regular,Roboto">
            {image}
            {progressBar}
        </svg>
'''
