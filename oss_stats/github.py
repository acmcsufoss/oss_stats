from github import Github
import os

token = os.getenv("GITHUB_TOKEN")
github = Github(token)

org = "acmcsufoss"


def fetch_repositories():
    repos = github.get_organization(org).get_repos()
    return [repo.name for repo in repos]


# TODO: Create functions that fetch issues, PRs, commits, number of contributors,
# and more from acmcsufoss org and EthanThatOneKid/acmcsuf.com using the PyGithub library.
def fetch_prs():
    repos = github.get_organization(org).get_repos()
    num_PRs = 0
    # Loops through each repo and counts PRs
    for repo in repos:
        num_PRs += repo.get_pulls(state="open").totalCount
        num_PRs += repo.get_pulls(state="closed").totalCount
        
    return num_PRs

