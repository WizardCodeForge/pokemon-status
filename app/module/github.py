from service.github import get_basic_metrics
from type.github_service import MetricsDTO


def get_xp_by_github(user: str) -> int:
    metrics: MetricsDTO = get_basic_metrics(user)

    xp = 0

    xp += metrics['all_commits'] * 3
    xp += metrics['all_followers'] * 4
    xp += metrics['all_forks'] * 7
    xp += metrics['all_issues'] * 2
    xp += metrics['all_prs'] * 2
    xp += metrics['all_prs_review'] * 3
    xp += metrics['all_repos'] * 3
    xp += metrics['all_stars'] * 7

    return xp
