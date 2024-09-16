from typing import TypedDict


class MetricsDTO(TypedDict):
    all_commits: int
    all_repos: int
    all_followers: int
    all_stars: int
    all_issues: int
    all_prs: int
    all_prs_review: int
    all_forks: int
