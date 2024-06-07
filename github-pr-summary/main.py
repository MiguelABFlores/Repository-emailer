# Importing from the modular files of the project
from github_api import fetch_pull_requests
from console_formatter import format_console_body
from html_formatter import format_html_body
from html_generator import generate_html_report
from config import REPO_OWNER, REPO_NAME, EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT


def main():
    # Fetching the json from the repository and calling the function
    opened_prs = fetch_pull_requests(REPO_OWNER, REPO_NAME, 'open')
    closed_prs = fetch_pull_requests(REPO_OWNER, REPO_NAME, 'closed')
    # Filter of the merged PR's and the closed ones
    merged_prs = [pr for pr in closed_prs if pr['merged_at'] is not None]
    closed_prs = [pr for pr in closed_prs if pr['merged_at'] is None]

    # Format the email body with the pull request data
    email_console_body = format_console_body(REPO_NAME, opened_prs, merged_prs, closed_prs)

    # Printing the email content to console
    print("From:", EMAIL_FROM)
    print("To:", EMAIL_TO)
    print("Subject:", EMAIL_SUBJECT)
    print("\nBody:\n", email_console_body)

if __name__ == "__main__":
    main()
