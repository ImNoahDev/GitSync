# GitHub to Gitea Mirror

This Docker container automatically mirrors your GitHub repositories to a Gitea instance.

## Features

- Mirrors all repositories (including private ones) from GitHub to Gitea
- Runs every 5 minutes to check for updates
- Easy setup using environment variables

## Prerequisites

- Docker installed on your system
- GitHub account and personal access token
- Gitea instance and API token

## Usage

1. Pull the Docker image from Docker Hub:

   ```
   docker pull lecodyman/gitsync:latest
   ```

2. Run the container:

   ```
   docker run -d --name github-gitea-mirror \
     -e GITHUB_USERNAME=your-github-username \
     -e GITHUB_TOKEN=your-github-token \
     -e GITEA_URL=http://your-gitea-domain/api/v1 \
     -e GITEA_TOKEN=your-gitea-token \
     -e GITEA_UID=1 \
     lecodyman/gitsync:latest
   ```

   Replace the placeholder values with your actual credentials and URLs.

## Optional: Build from Source

If you prefer to build the image from source:

1. Clone the repository:

   ```
   git clone https://github.com/your-repo/github-gitea-mirror.git
   cd github-gitea-mirror
   ```

2. Build the Docker image:

   ```
   docker build -t github-gitea-mirror .
   ```

3. Run the container using the locally built image:

   ```
   docker run -d --name github-gitea-mirror \
     -e GITHUB_USERNAME=your-github-username \
     -e GITHUB_TOKEN=your-github-token \
     -e GITEA_URL=http://your-gitea-domain/api/v1 \
     -e GITEA_TOKEN=your-gitea-token \
     -e GITEA_UID=1 \
     github-gitea-mirror
   ```

## Environment Variables

- `GITHUB_USERNAME`: Your GitHub username
- `GITHUB_TOKEN`: Your GitHub personal access token
- `GITEA_URL`: The API URL of your Gitea instance
- `GITEA_TOKEN`: Your Gitea API token
- `GITEA_UID`: The user ID in Gitea where repositories will be mirrored (typically 1 for admin)
- `RECHECK_TIME`: The frequency (in minutes) at which the container will check for updates (default is 5 minutes)

## How it Works

The container runs a Python script (`main.py`) that:

1. Fetches all repositories from your GitHub account
2. For each repository, creates a mirrored repository in Gitea
3. Repeats this process every 5 minutes to keep everything in sync

## Troubleshooting

If you encounter any issues, check the container logs:
