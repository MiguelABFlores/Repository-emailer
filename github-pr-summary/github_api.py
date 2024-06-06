# Libraries and dependencies, required installations will be added when creating the Docker Image
import requests # Library used to handle http requests for the API
# pip3 install PyGithub requests
from datetime import datetime, timedelta # Library used to use easier date and time

LAST_WEEK = (datetime.now() - timedelta(days = 7)).isoformat() # ISOFORMAT
# The ISO format helps to add the date in digits for easier handling

# Main Function to fetch the Pull Requests from the repository
def fetch_pull_requests(repo_owner, repo_name, state):
    github_api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls'
    '''
    Chosen public active repository
    https://github.com/huggingface/text-generation-inference
    https://api.github.com/repos/huggingface/text-generation-inference/pulls
    Getting the json from this we can see what to expect from different parameters
    PR for testing: https://github.com/huggingface/text-generation-inference/pull/1985
    '''
    # Basic fetch parameters
    params = {
        'state': state, # can be open, merged or closed
        'sort': 'created', # sort by creation time
        'direction': 'desc', # sort in descending order
        'since': LAST_WEEK,
    }
    response = requests.get(github_api_url, params=params) # Do the GET request to the GITHUB_API_URL provided in the parameters
    response.raise_for_status() # Error status if not fetching correctly
    return response.json() # Return the Json from the API of the pull requests
