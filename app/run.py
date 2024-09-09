from modules.pokemon import get_pokemon
from modules.github import get_github_metrics
import requests_cache
from flask import Flask, request
from dotenv import load_dotenv


load_dotenv("./infra/envs/.env")
app = Flask(__name__)
requests_cache.install_cache("pokemon_cache", expire_after=100)


@app.route('/', methods=['GET'])
def home():
    args = request.args
    user = args.get("user")
    pokemon = args.get("pokemon")

    metrics = get_github_metrics(user)
    pokemon = get_pokemon(args.get("pokemon"), metrics["all_commits"])
    return metrics, 200


if __name__ == '__main__':
    app.run(port=8088)
