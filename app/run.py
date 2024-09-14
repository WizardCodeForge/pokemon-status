from modules.pokemon import get_pokemon
from modules.github import get_xp_by_github
from service.svgDraw import get_svg_draw
from flask import Flask, request, Response
from dotenv import load_dotenv


load_dotenv("./infra/envs/.env")
app = Flask(__name__)


@app.route('/', methods=['GET'])
def render():
    args = request.args
    user = args.get("user")
    pokemon = args.get("pokemon") or "charmander"

    metrics = get_xp_by_github(user)
    pokeDTO = get_pokemon(pokemon, metrics['all_repos'])
    svg_content = get_svg_draw(pokeDTO)

    return Response(svg_content, mimetype='image/svg+xml')


if __name__ == '__main__':
    app.run(port=8088)
