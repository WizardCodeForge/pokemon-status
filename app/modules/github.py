from service.github import get_basic_metrics
from type.github_service import MetricsDTO


def get_xp_by_github(user: str) -> MetricsDTO:
    metrics: MetricsDTO = get_basic_metrics(user)

    return metrics
