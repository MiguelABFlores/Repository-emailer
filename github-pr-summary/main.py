# Main File: The main script that coordinates fetching the pull requests and formatting the email body for the project
# Libraries
import requests
from datetime import datetime, timedelta

# Parameters for the code
REPO_OWNER = 'huggingface'
REPO_NAME = 'text-generation-inference'
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls'
# Chosen public active repository
# https://github.com/huggingface/text-generation-inference
# https://api.github.com/repos/huggingface/text-generation-inference/pulls
LAST_WEEK = (datetime.now() - timedelta(days=7)).isoformat()

# Email Information for the Scrum Master
EMAIL_FROM = 'miiguelb07@gmail.com'
EMAIL_TO = 'miiguelb07@gmail.com'
EMAIL_SUBJECT = f'Weekly Pull Request Summary for {REPO_NAME}'

def main():
    # instructions fetch the pr

