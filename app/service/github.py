import requests
from type.github_service import ReposDTO
import os

header = {"auth": os.environ.get("GITHUB_TOKEN", "Nada")}


def get_repos(user: str) -> list[ReposDTO]:
    url = f"https://api.github.com/users/{user}/repos"
    repos = []
    page = 1

    while True:
        params = {'per_page': 100, 'page': page}
        resp = requests.get(url, params=params, headers=header)
        resp.raise_for_status()
        data = resp.json()

        if not data:
            break

        for r in data:
            dto: ReposDTO = {
                "name": r["name"],
                "stars": r["stargazers_count"],
            }
            repos.append(dto)

        page += 1

    return repos


def commit_count(user: str, repo_name: str) -> int:
    url = f'https://api.github.com/repos/{user}/{repo_name}/commits'
    total_commits = 0
    page = 1

    while True:
        params = {'per_page': 100, 'page': page}

        resp = requests.get(url, params=params, headers=header)
        resp.raise_for_status()
        data = resp.json()

        if not data:  # Se não houver mais commits, saímos do loop
            break
        total_commits += len(data)
        page += 1

    return total_commits


def get_followers(usuario):
    url = f'https://api.github.com/users/{usuario}'

    resp = requests.get(url, headers=header)
    resp.raise_for_status()
    data = resp.json()
    return data.get('followers', 0)
