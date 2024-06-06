def format_email_body(repo_name, opened_prs, merged_prs, closed_prs):
    # Format the email body with the pull requests count
    # To count the number of items we are just using len which calculates the length of a list given
    # So we are just pointing to the lists of opened and closed prs
    email_body = f"Weekly Pull Request Summary for {repo_name} repository\n\n"
    email_body += f"Total PRs opened in the last week: {len(opened_prs)}\n"
    email_body += f"Total PRs merged in the last week: {len(merged_prs)}\n"
    email_body += f"Total PRs closed in the last week: {len(closed_prs)}\n\n"

    # List all the opened Pull Requests
    # Here we are iterating item by item and add to the body the parameters we are looking for from the GitHub API
    # I want to make it as a list so it will be initiated with a -
    email_body += "Opened Pull Requests:\n"
    for pr in opened_prs:
        email_body += f"- title: {pr['title']} | by: {pr['user']['login']} | number: #{pr['number']}\n"
        email_body += f"  url: {pr['html_url']}\n"

    email_body += "\nMerged Pull Requests:\n"
    for pr in merged_prs:
        email_body += f"- title: {pr['title']} | by: {pr['user']['login']} | number: #{pr['number']}\n"
        email_body += f"  url: {pr['html_url']}\n"

    email_body += "\nClosed Pull Requests:\n"
    for pr in closed_prs:
        email_body += f"- title: {pr['title']} | by: {pr['user']['login']} | number: #{pr['number']}\n"
        email_body += f"  url: {pr['html_url']}\n"

    return email_body
