import os
import re
import time

# Naye Post Ka Data
title = "GTA 5 Black Screen Fix Opening Mission"
username = "gamer_pro99"
content = "Go to graphics settings, change DirectX 12 to DirectX 11, and update GPU drivers."

# Clean Permanent SEO Slug
slug = title.lower()
slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
timestamp = int(time.time())
file_name = f"{slug}-{timestamp}.html"

os.makedirs("posts", exist_ok=True)
file_path = os.path.join("posts", file_name)

# Template Replace
with open("template.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("{{TITLE}}", title)\
           .replace("{{DESCRIPTION}}", content[:150])\
           .replace("{{USERNAME}}", username)\
           .replace("{{CONTENT}}", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

# 🎯 Real HTML Link Injected (No Hash #)
new_post_card = f'''
<div class="card" onclick="window.location.href='posts/{file_name}'">
    <div class="card-header">
        <div class="author-info">
            <div class="avatar" style="background: linear-gradient(135deg, #ef4444, #f97316);">G</div>
            <div>
                <div class="author-name">@{username}</div>
                <div class="meta-text">Posted in l/community • Just now</div>
            </div>
        </div>
        <span class="tag">Gaming & Setup</span>
    </div>
    <div class="post-title"><a href="posts/{file_name}" style="color: inherit; text-decoration: none;">{title}</a></div>
    <div class="post-body">{content[:110]}...</div>
</div>
'''

# Read index.html and insert before container end
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

if '<div id="postsContainer">' in index_content:
    index_content = index_content.replace('<div id="postsContainer">', f'<div id="postsContainer">\n{new_post_card}')
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)

print(f"✅ Real Static Page Ban Gaya: posts/{file_name}")