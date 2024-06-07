import os

def generate_html_report(html_content, report_path='/report/github-pr-summary.html'):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    # Write the HTML content to the file
    with open(report_path, 'w') as file:
        file.write(html_content)

    print(f"HTML report generated and saved to {report_path}")
