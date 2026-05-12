#!/usr/bin/env python3
import markdown
import os

# Read all markdown files
files = [
    '00_executive_summary.md',
    '01_market_analysis.md',
    '02_financial_models.md',
    '03_macro_analysis.md',
    '04_policy_analysis.md',
    '05_appendix.md'
]

base_path = '/Users/maekaess/CascadeProjects/windsurf-project/'
combined_content = ""

for filename in files:
    filepath = os.path.join(base_path, filename)
    with open(filepath, 'r') as f:
        content = f.read()
        # Add page break before each section except the first
        if filename != files[0]:
            combined_content += '<div class="page-break"></div>\n'
        combined_content += content

# Convert markdown to HTML
html_content = markdown.markdown(combined_content, extensions=['tables', 'fenced_code'])

# Create full HTML document with CSS styling
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Intergenerational Mobility Fund — Enhanced Proposal</title>
    <style>
        @page {{
            size: letter;
            margin: 0.75in;
        }}
        body {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
            margin: 0;
            padding: 0;
            font-size: 11pt;
        }}
        .container {{
            max-width: 8.5in;
            margin: 0 auto;
            padding: 0;
        }}
        h1 {{
            color: #1a365d;
            border-bottom: 3px solid #2b6cb0;
            padding-bottom: 10px;
            page-break-after: avoid;
            margin-top: 40px;
        }}
        h2 {{
            color: #2c5282;
            border-bottom: 2px solid #4299e1;
            padding-bottom: 8px;
            page-break-after: avoid;
            margin-top: 30px;
        }}
        h3 {{
            color: #2b6cb0;
            page-break-after: avoid;
            margin-top: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            page-break-inside: avoid;
            font-size: 10pt;
        }}
        th {{
            background-color: #ebf8ff;
            color: #1a365d;
            font-weight: bold;
            padding: 12px 8px;
            text-align: left;
            border: 1px solid #cbd5e0;
        }}
        td {{
            padding: 10px 8px;
            border: 1px solid #e2e8f0;
        }}
        tr:nth-child(even) {{
            background-color: #f7fafc;
        }}
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 5px 0;
        }}
        p {{
            margin: 10px 0;
        }}
        strong {{
            color: #1a365d;
        }}
        em {{
            color: #4a5568;
        }}
        .page-break {{
            page-break-before: always;
            height: 0;
        }}
        code {{
            background-color: #f7fafc;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        hr {{
            border: none;
            border-top: 2px solid #e2e8f0;
            margin: 30px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_content}
    </div>
</body>
</html>
"""

# Save HTML file
output_path = os.path.join(base_path, 'intergenerational_mobility_fund.html')
with open(output_path, 'w') as f:
    f.write(full_html)

print(f"HTML generated successfully: {output_path}")
print("Open this file in your browser (Chrome, Safari, Firefox) and use File > Print > Save as PDF")
