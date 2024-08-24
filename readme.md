# GitHub to Gitea Repository Automatic Mirror

This Python script automates the process of mirroring GitHub repositories to a Gitea instance. It fetches all repositories (including private ones) from a GitHub account and creates corresponding mirror repositories in Gitea.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- GitHub account and personal access token
- Gitea instance and API token
- Gitea user ID (typically 1 for admin, but verify)

## Configuration

Before running the script, update the following variables in `main.py`:

- `github_username`: Your GitHub username
- `github_token`: Your GitHub personal access token
- `gitea_url`: The base URL of your Gitea API (e.g., "http://your-gitea-domain/api/v1")
- `gitea_token`: Your Gitea API token
- `gitea_uid`: The user ID in Gitea where repositories will be created (typically 1 for admin)

## Usage

1. Ensure all prerequisites are met and configuration variables are set.
2. Run the script:

   ```
   python main.py
   ```

3. The script will iterate through all your GitHub repositories and create mirror repositories in Gitea.

## Output

The script will print the status of each repository mirroring operation:

- Success: "Successfully mirrored {repo_name}"
- Failure: "Failed to mirror {repo_name}: {error_message}"

## Automating with Cron

To run this script automatically at regular intervals, you can use cron on Unix-based systems. Here's how to set it up:

1. Open your crontab file:

   ```
   crontab -e
   ```

2. Add a line to schedule the script. For example, to run it every hour:

   ```
   0 * * * * /usr/bin/python3 /path/to/your/main.py >> /path/to/logfile.log 2>&1
   ```

   Replace `/path/to/your/main.py` with the actual path to your script, and `/path/to/logfile.log` with where you want to store the log output.

3. Save and exit the crontab editor.

Make sure the script has the necessary permissions to run and that all paths are absolute.

Note: When running via cron, ensure that environment variables or configuration files are properly set up, as the cron environment may differ from your interactive shell environment.


## Notes

- This script mirrors all repositories, including private ones.
- Ensure your Gitea instance has sufficient storage and your account has the necessary permissions.
- Be mindful of API rate limits for both GitHub and Gitea.

## License

[Specify your license here]

## Contributing

[Add contribution guidelines if applicable]