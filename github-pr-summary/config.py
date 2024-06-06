# Configuration details
import os

# Repository Configuration details
REPO_OWNER = os.getenv('huggingface')
REPO_NAME = os.getenv('text-generation-inference')

# Email Information for the Scrum Master
EMAIL_FROM = os.getenv('no-reply@someemail.com')
EMAIL_TO = os.getenv('tosomeone@someemail.com')
EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT', f'Weekly PR Summary for {REPO_NAME}')

'''
Chosen public active repository:
https://github.com/huggingface/text-generation-inference
https://api.github.com/repos/huggingface/text-generation-inference/pulls
Getting the json from this we can see what to expect from different parameters
PR for testing: https://github.com/huggingface/text-generation-inference/pull/1985
'''
