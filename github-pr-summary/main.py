# Main File: The main script that coordinates fetching the pull requests and formatting the email body for the project
# Libraries and dependencies, required installations will be added when creating the Docker Image
import requests # Library used to handle http requests for the API
# pip3 install PyGithub requests
from datetime import datetime, timedelta # Library used to use easier date and time

# Parameters for the code
REPO_OWNER = 'huggingface'
REPO_NAME = 'text-generation-inference'
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls'
# Chosen public active repository
# https://github.com/huggingface/text-generation-inference
# https://api.github.com/repos/huggingface/text-generation-inference/pulls
# Getting the json from this we can see what to expect from different parameters
# PR for testing: https://github.com/huggingface/text-generation-inference/pull/1985
LAST_WEEK = (datetime.now() - timedelta(days=7)).isoformat() # ISOFORMAT https://www.geeksforgeeks.org/isoformat-method-of-datetime-class-in-python/

# Email Information for the Scrum Master
EMAIL_FROM = 'miiguelb07@gmail.com'
EMAIL_TO = 'miiguelb07@gmail.com'
EMAIL_SUBJECT = f'Weekly PR Summary for {REPO_NAME}'

# Main Function to fetch the Pull Requests from the repository
def fetch_pull_requests(state):
    # Basic fetch parameters
    params = {
        'state': state,
        'sort': 'created',
        'direction': 'desc',
        'since': LAST_WEEK,
    }
    #
    response = requests.get(GITHUB_API_URL, params=params)
    response.raise_for_status()
    return response.json()
