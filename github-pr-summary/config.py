# Configuration details
import os

# Repository Configuration details
REPO_OWNER = os.getenv('REPO_OWNER', 'huggingface')
REPO_NAME = os.getenv('REPO_NAME', 'text-generation-inference')

# Email Information for the Scrum Master
EMAIL_FROM = os.getenv('EMAIL_FROM', 'no-reply@someemail.com')
EMAIL_TO = os.getenv('EMAIL_TO', 'tosomeone@someemail.com')
EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT', f'Weekly PR Summary for {REPO_NAME}')

'''
Chosen public active repository:
https://github.com/huggingface/text-generation-inference
https://api.github.com/repos/huggingface/text-generation-inference/pulls
Getting the json from this we can see what to expect from different parameters
PR for testing: https://github.com/huggingface/text-generation-inference/pull/1985
'''
