import os
import time
import requests
import schedule
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def mirror_repos():
    github_username = os.environ['GITHUB_USERNAME']
    github_token = os.environ['GITHUB_TOKEN']
    gitea_url = os.environ['GITEA_URL']
    gitea_token = os.environ['GITEA_TOKEN']
    gitea_uid = int(os.environ.get('GITEA_UID', '1'))  # Default to 1 if not set

    headers = {
        "Authorization": f"token {gitea_token}",
        "Content-Type": "application/json"
    }

    # Fetch all repositories, including private ones
    logging.info("Fetching repositories from GitHub")
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
            "auth_password": github_token
        }

        logging.info(f"Attempting to mirror repository: {repo_name}")
        response = requests.post(f"{gitea_url}/repos/migrate", json=mirror_payload, headers=headers)

        if response.status_code == 201:
            logging.info(f"Successfully mirrored {repo_name}")
        else:
            logging.error(f"Failed to mirror {repo_name}: {response.content}")

def run_scheduler():
    recheck_time = int(os.environ.get('RECHECK_TIME', 5))  # Default to 5 minutes if not set
    logging.info(f"Scheduler set to run every {recheck_time} minutes")
    schedule.every(recheck_time).minutes.do(mirror_repos)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    logging.info("Starting the repository mirroring service")
    run_scheduler()