FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir requests

CMD ["pyhton", "/github-pr-summary/main.py"]
