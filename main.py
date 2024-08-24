import requests

github_username = "your-github-username" 
github_token = "your-github-token"
gitea_url = "http://your-gitea-domain/api/v1"
gitea_token = "your-gitea-token"
gitea_uid = 1  # Typically, the Gitea admin user has UID 1, but verify if different.

headers = {
    "Authorization": f"token {gitea_token}",
    "Content-Type": "application/json"
}

# Fetch all repositories, including private ones
github_repos = requests.get(
    f"https://api.github.com/user/repos?visibility=all",
    auth=(github_username, github_token)
).json()

for repo in github_repos:
    repo_name = repo["name"]
    is_private = repo["private"]

    mirror_payload = {
        "clone_addr": repo["clone_url"],
        "uid": gitea_uid,
        "repo_name": repo_name,
        "mirror": True,
        "private": is_private,
        "auth_username": github_username,
        "auth_password": github_token  # This ensures the private repos are accessible.
    }

    response = requests.post(f"{gitea_url}/repos/migrate", json=mirror_payload, headers=headers)

    if response.status_code == 201:
        print(f"Successfully mirrored {repo_name}")
    else:
        print(f"Failed to mirror {repo_name}: {response.content}")
