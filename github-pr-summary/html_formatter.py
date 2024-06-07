def format_html_body(repo_name, opened_prs, merged_prs, closed_prs):
    html_body = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Weekly Pull Request Summary for {repo_name}</h1>
        <p>Total PRs opened in the last week: {len(opened_prs)}</p>
        <p>Total PRs merged in the last week: {len(merged_prs)}</p>
        <p>Total PRs closed in the last week: {len(closed_prs)}</p>

        <h2>Opened Pull Requests</h2>
        <table>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Number</th>
                <th>URL</th>
            </tr>
    """
    for pr in opened_prs:
        html_body += f"""
            <tr>
                <td>{pr['title']}</td>
                <td>{pr['user']['login']}</td>
                <td>#{pr['number']}</td>
                <td><a href="{pr['html_url']}">Link</a></td>
            </tr>
        """

    html_body += """
        </table>
        <h2>Merged Pull Requests</h2>
        <table>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Number</th>
                <th>URL</th>
            </tr>
    """
    for pr in merged_prs:
        html_body += f"""
            <tr>
                <td>{pr['title']}</td>
                <td>{pr['user']['login']}</td>
                <td>#{pr['number']}</td>
                <td><a href="{pr['html_url']}">Link</a></td>
            </tr>
        """

    html_body += """
        </table>
        <h2>Closed Pull Requests</h2>
        <table>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Number</th>
                <th>URL</th>
            </tr>
    """
    for pr in closed_prs:
        html_body += f"""
            <tr>
                <td>{pr['title']}</td>
                <td>{pr['user']['login']}</td>
                <td>#{pr['number']}</td>
                <td><a href="{pr['html_url']}">Link</a></td>
            </tr>
        """

    html_body += """
        </table>
    </body>
    </html>
    """
    return html_body
