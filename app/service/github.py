import requests
from type.github_service import MetricsDTO
import os


def get_basic_metrics(user: str) -> MetricsDTO:
    url = 'https://api.github.com/graphql'

    header = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}

    query = """
    query getAmount    {
        user(login: "%s") {
            contributionsCollection {
                totalCommitContributions,
                totalIssueContributions,
                totalPullRequestContributions,
                totalPullRequestReviewContributions
            },
            followers {
                totalCount 
            },
            repositories(isFork: false, first: 100) {
                nodes {
                    name,
                    stargazerCount,
                    forkCount
                }
            }
        }
    }
    """ % user

    res = requests.post(url, json={'query': query}, headers=header)
    res.raise_for_status()
    data = res.json()

    metrics: MetricsDTO = {"all_repos": 0, "all_stars": 0, "all_forks": 0}
    metrics["all_commits"] = data["data"]["user"]["contributionsCollection"]["totalCommitContributions"]
    metrics["all_issues"] = data["data"]["user"]["contributionsCollection"]["totalIssueContributions"]
    metrics["all_prs"] = data["data"]["user"]["contributionsCollection"]["totalPullRequestContributions"]
    metrics["all_prs_review"] = data["data"]["user"]["contributionsCollection"]["totalPullRequestReviewContributions"]
    metrics["all_followers"] = data["data"]["user"]["followers"]["totalCount"]

    for repos in data["data"]["user"]["repositories"]["nodes"]:
        metrics["all_repos"] += 1
        metrics["all_stars"] += repos["stargazerCount"]
        metrics["all_forks"] += repos["forkCount"]

    return metrics
