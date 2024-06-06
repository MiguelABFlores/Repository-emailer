# Libraries and dependencies, required installations will be added when creating the Docker Image
import requests # Library used to handle http requests for the API
# pip3 install PyGithub requests
from datetime import datetime, timedelta # Library used to use easier date and time

# Parameters for the code
REPO_OWNER = 'huggingface'
REPO_NAME = 'text-generation-inference'
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls'
'''
Chosen public active repository
https://github.com/huggingface/text-generation-inference
https://api.github.com/repos/huggingface/text-generation-inference/pulls
Getting the json from this we can see what to expect from different parameters
PR for testing: https://github.com/huggingface/text-generation-inference/pull/1985
'''
LAST_WEEK = (datetime.now() - timedelta(days = 7)).isoformat() # ISOFORMAT
# The ISO format helps to add the date in digits for easier handling

# Email Information for the Scrum Master
EMAIL_FROM = 'no-reply@someemail.com'
EMAIL_TO = 'tosomeone@someemail.com'
EMAIL_SUBJECT = f'Weekly PR Summary for {REPO_NAME}'

# Main Function to fetch the Pull Requests from the repository
def fetch_pull_requests(state):
    # Basic fetch parameters
    params = {
        'state': state, # can be open, merged or closed
        'sort': 'created', # sort by creation time
        'direction': 'desc', # sort in descending order
        'since': LAST_WEEK,
    }
    response = requests.get(GITHUB_API_URL, params=params) #Do the GET request to the GITHUB_API_URL provided in the parameters
    response.raise_for_status() # Error status if not fetching correctly
    return response.json() # Return the Json from the API of the pull requests

# Fetching the json from the repository and calling the function
opened_prs = fetch_pull_requests('open')
closed_prs = fetch_pull_requests('closed')

# We create one list with the open and closed prs in the retrieved json
# Each list comes in form of a list of dictionaries, so it is possible to combine them
# We just need to concatenate open and closed lists with +
all_prs = opened_prs + closed_prs

# Separate all the PRs, we are getting only the Last Week PRs as requested
'''
First we will make the iterations and then the conditions that should be met
Then we will iterate item to item in the previously created combined list 'all_prs'
*When iterating we are adding all the prs that are within a week from todays date (7 days), others are discarded
By the end of the list we will have filtered all the prs that are 1 week old, so instead of having a thousand list
we will be having a list of, for example 10
'''
prs_last_week = [pr for pr in all_prs if datetime.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ') > datetime.now() - timedelta(days=7)]

# Format the email body with the pull requests count
# To count the number of items we are just using len which calculates the length of a list given
# So we are just pointing to the lists of opened and closed prs
email_body = f"Weekly Pull Request Summary for {REPO_NAME} repository\n\n"
email_body += f"Total PRs opened in the last week: {len(opened_prs)}\n"
email_body += f"Total PRs closed in the last week: {len(closed_prs)}\n\n"

# List all the opened Pull Requests
# Here we are iterating item by item and add to the body the parameters we are looking for from the GitHub API
# I want to make it as a list so it will be initiated with a -
email_body += "Opened Pull Requests:\n"
for pr in opened_prs:
    email_body += f"- title: {pr['title']} | by: {pr['user']['login']} | number: #{pr['number']}\n"
    email_body += f"  url: {pr['html_url']}\n"

email_body += "\nClosed Pull Requests:\n"
for pr in closed_prs:
    email_body += f"- title: {pr['title']} | by: {pr['user']['login']} | number: #{pr['number']}\n"
    email_body += f"  url: {pr['html_url']}\n"

# Printing the email content to console
print("From:", EMAIL_FROM)
print("To:", EMAIL_TO)
print("Subject:", EMAIL_SUBJECT)
print("\nBody:\n", email_body)
