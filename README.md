# repository-emailer

Project to retrieve from the GitHub API the data needed to summarize the pull requests from a public repository, after data has been retrieved it will generate a report and send it to the email of a scrum master.

# Requirements

Dependencies needed:

- requests
  ```
  pip3 install PyGithub requests
  ```

# Sources

- [using-github-api-in-python](https://thepythoncode.com/article/using-github-api-in-python)
- [Isoformat() Method Of Datetime Class In Python](https://www.geeksforgeeks.org/isoformat-method-of-datetime-class-in-python/)
- [GitHub API Docs](https://docs.github.com/en/rest/pulls?apiVersion=2022-11-28)
- [GitHub API Docs PR](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests)
