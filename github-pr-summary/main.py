# Importing from the modular files of the project
from github_api import fetch_pull_requests
from email_formatter import format_email_body
from config import REPO_OWNER, REPO_NAME, EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT

def main():
    # Fetching the json from the repository and calling the function
    opened_prs = fetch_pull_requests(REPO_OWNER, REPO_NAME, 'open')
    closed_prs = fetch_pull_requests(REPO_OWNER, REPO_NAME, 'closed')

    # Format the email body with the pull request data
    email_body = format_email_body(REPO_NAME, opened_prs, closed_prs)

    # Printing the email content to console
    print("From:", EMAIL_FROM)
    print("To:", EMAIL_TO)
    print("Subject:", EMAIL_SUBJECT)
    print("\nBody:\n", email_body)

if __name__ == "__main__":
    main()
