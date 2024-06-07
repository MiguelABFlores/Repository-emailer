# ht
def format_html_body(repo_name, opened_prs, merged_prs, closed_prs):
    total_prs = len(opened_prs) + len(merged_prs) + len(closed_prs)
    opened_percentage = (len(opened_prs) / total_prs) * 100 if total_prs else 0
    merged_percentage = (len(merged_prs) / total_prs) * 100 if total_prs else 0
    closed_percentage = (len(closed_prs) / total_prs) * 100 if total_prs else 0

    html_body = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #333333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                padding: 12px;
                border: 1px solid #dddddd;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
                color: #333333;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            .opened {{
                color: #4CAF50;
            }}
            .merged {{
                color: #2196F3;
            }}
            .closed {{
                color: #f44336;
            }}
            .chart-container {{
                width: 50%;
                margin: auto;
            }}
        </style>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <div class="container">
            <h1>Weekly Pull Request Summary for {repo_name}</h1>
            <p>Total PRs opened in the last week: <span class="opened">{len(opened_prs)}</span></p>
            <p>Total PRs merged in the last week: <span class="merged">{len(merged_prs)}</span></p>
            <p>Total PRs closed in the last week: <span class="closed">{len(closed_prs)}</span></p>

            <div class="chart-container">
                <canvas id="prChart"></canvas>
            </div>

            <script>
                var ctx = document.getElementById('prChart').getContext('2d');
                var prChart = new Chart(ctx, {{
                    type: 'pie',
                    data: {{
                        labels: ['Opened', 'Merged', 'Closed'],
                        datasets: [{{
                            data: [{opened_percentage}, {merged_percentage}, {closed_percentage}],
                            backgroundColor: ['#4CAF50', '#2196F3', '#f44336'],
                            hoverBackgroundColor: ['#66BB6A', '#42A5F5', '#EF5350']
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        legend: {{
                            position: 'top',
                        }},
                        title: {{
                            display: true,
                            text: 'Pull Request Status Distribution'
                        }},
                        animation: {{
                            animateScale: true,
                            animateRotate: true
                        }}
                    }}
                }});
            </script>

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
        </div>
    </body>
    </html>
    """

    return html_body
