FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Working directory to the folder containing main.py
WORKDIR /usr/src/app/github-pr-summary

# Run the script
CMD ["python", "./main.py"]
