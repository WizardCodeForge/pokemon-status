from app.module import get_xp_by_github, get_pokemon, get_svg_banner
from flask import Flask, request, Response
from dotenv import load_dotenv


load_dotenv("./infra/envs/.env")
app = Flask(__name__)


@app.route('/', methods=['GET'])
def render():
    args = request.args
    user = args.get("user") or "CriticalNoob02"
    pokemon = args.get("pokemon") or "charmander"
    theme = args.get("theme") or "charmander"

    xp = get_xp_by_github(user)
    pokeDTO = get_pokemon(pokemon, xp)
    svg_content = get_svg_banner(pokeDTO, theme)

    return Response(svg_content, mimetype='image/svg+xml')
