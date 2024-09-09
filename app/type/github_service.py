from typing import TypedDict


class ReposDTO(TypedDict):
    name: str
    stars: int


class MetricsDTO(TypedDict):
    all_commits: int
    all_repos: int
    all_followers: int
    all_stars: int
