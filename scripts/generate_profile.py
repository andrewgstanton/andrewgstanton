import markdown
from pathlib import Path
from datetime import datetime
	
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# Paths
base_path = Path("/app")	
profile_md_path = base_path / "profile" / "bio.md"
readme_path = base_path / "README.md"
index_path = base_path / "docs" / "index.html"

# Load markdown content
with open(profile_md_path, "r", encoding="utf-8") as f:
    profile_md = f.read()

# Generate README.md (direct copy)
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(profile_md)
	
readme_footer = f"\n---\n_Last generated: **{timestamp}**_\n"
with open(readme_path, "a") as f:
    f.write(readme_footer)

# Generate index.html
html_body = markdown.markdown(profile_md)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Andrew G. Stanton</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            font-family: "Segoe UI", Tahoma, sans-serif;
            background: #f9f9f9;
            color: #222;
            padding: 2rem;
            max-width: 800px;
            margin: auto;
            line-height: 1.6;
        }}
        h1, h2 {{
            color: #333;
        }}
        a {{
            color: #0066cc;
        }}
    </style>
</head>
<body>
{html_body}
<section>
    <h2>Résumé</h2>
    <p>
        Download my full résumé (PDF): 
        <a href="andrewgstanton_resume_2025.pdf" target="_blank">andrewgstanton_resume_2025.pdf</a>
    </p>
</section>
</body>
</html>"""
	
html_footer = f"""
<footer>
    <hr>
    <small>Last generated: <strong>{timestamp}</strong></small>
</footer>
"""
html_template = html_template.replace("</body>", f"{html_footer}</body>")

	
index_path.parent.mkdir(parents=True, exist_ok=True)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print("README.md and docs/index.html have been generated.")
