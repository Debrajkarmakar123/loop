import os
import time

# Naye Post Ka Data
title = "GTA 5 Black Screen Fix Opening Mission"
username = "gamer_pro99"
content = "Go to graphics settings, change DirectX 12 to DirectX 11, and update GPU drivers."

# Auto File Generator
timestamp = int(time.time())
file_name = f"gta5-fix-{timestamp}.html"

os.makedirs("posts", exist_ok=True)
file_path = os.path.join("posts", file_name)

with open("template.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("{{TITLE}}", title)\
           .replace("{{DESCRIPTION}}", content[:150])\
           .replace("{{USERNAME}}", username)\
           .replace("{{CONTENT}}", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Naya Static Page Ban Gaya: {file_path}")