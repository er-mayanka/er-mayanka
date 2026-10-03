import json
import os

# Read stats from GitHub Actions output (may be double-encoded)
stats_raw = os.environ.get('STATS', '{}')
try:
    s = json.loads(stats_raw)
    # If it's a string, parse again
    if isinstance(s, str):
        s = json.loads(s)
except:
    s = {}

trophies = []

# Stars trophies
if s.get('totalStars', 0) >= 1000:
    trophies.append(('💎', 'Diamond', f"{s['totalStars']:,} stars"))
elif s.get('totalStars', 0) >= 500:
    trophies.append(('💠', 'Ruby', f"{s['totalStars']:,} stars"))
elif s.get('totalStars', 0) >= 100:
    trophies.append(('⭐', 'Star Gazer', f"{s['totalStars']:,} stars"))
elif s.get('totalStars', 0) >= 50:
    trophies.append(('✨', 'Rising Star', f"{s['totalStars']:,} stars"))
elif s.get('totalStars', 0) >= 10:
    trophies.append(('🌟', 'Stargazer', f"{s['totalStars']:,} stars"))

# Commits trophies
if s.get('totalCommits', 0) >= 10000:
    trophies.append(('🔥', 'Fire', f"{s['totalCommits']:,} commits"))
elif s.get('totalCommits', 0) >= 5000:
    trophies.append(('⚡', 'Lightning', f"{s['totalCommits']:,} commits"))
elif s.get('totalCommits', 0) >= 1000:
    trophies.append(('📝', 'Scribe', f"{s['totalCommits']:,} commits"))
elif s.get('totalCommits', 0) >= 500:
    trophies.append(('✍️', 'Writer', f"{s['totalCommits']:,} commits"))

# PRs trophies
if s.get('mergedPRs', 0) >= 500:
    trophies.append(('🔀', 'Merger', f"{s['mergedPRs']} PRs merged"))
elif s.get('mergedPRs', 0) >= 100:
    trophies.append(('🤝', 'Collaborator', f"{s['mergedPRs']} PRs merged"))
elif s.get('mergedPRs', 0) >= 50:
    trophies.append(('🔄', 'Contributor', f"{s['mergedPRs']} PRs merged"))

# Issues trophies
if s.get('closedIssues', 0) >= 200:
    trophies.append(('🐛', 'Bug Hunter', f"{s['closedIssues']} issues closed"))
elif s.get('closedIssues', 0) >= 50:
    trophies.append(('🔧', 'Fixer', f"{s['closedIssues']} issues closed"))

# Followers trophies
if s.get('followers', 0) >= 1000:
    trophies.append(('👑', 'Influencer', f"{s['followers']:,} followers"))
elif s.get('followers', 0) >= 500:
    trophies.append(('🌟', 'Popular', f"{s['followers']:,} followers"))
elif s.get('followers', 0) >= 100:
    trophies.append(('👥', 'Social', f"{s['followers']:,} followers"))
elif s.get('followers', 0) >= 50:
    trophies.append(('🤝', 'Connected', f"{s['followers']:,} followers"))

# Repos trophies
if s.get('publicRepos', 0) >= 50:
    trophies.append(('📦', 'Packager', f"{s['publicRepos']} repositories"))
elif s.get('publicRepos', 0) >= 20:
    trophies.append(('🏗️', 'Builder', f"{s['publicRepos']} repositories"))
elif s.get('publicRepos', 0) >= 10:
    trophies.append(('🛠️', 'Creator', f"{s['publicRepos']} repositories"))

# Account age
if s.get('accountAge', 0) >= 10:
    trophies.append(('🏛️', 'Veteran', f"{s['accountAge']} years on GitHub"))
elif s.get('accountAge', 0) >= 5:
    trophies.append(('🎖️', 'Senior', f"{s['accountAge']} years on GitHub"))
elif s.get('accountAge', 0) >= 3:
    trophies.append(('🥈', 'Experienced', f"{s['accountAge']} years on GitHub"))

# Contributions streak (approximate from total)
if s.get('totalContributions', 0) >= 5000:
    trophies.append(('📅', 'Streak Master', f"{s['totalContributions']:,} contributions"))
elif s.get('totalContributions', 0) >= 1000:
    trophies.append(('📈', 'Consistent', f"{s['totalContributions']:,} contributions"))

# Top languages badge
if s.get('topLangs'):
    trophies.append(('💻', 'Polyglot', s['topLangs']))

# Generate SVG
cols = 3
rows = (len(trophies) + cols - 1) // cols
cell_w, cell_h = 200, 80
padding = 15
width = cols * cell_w + (cols + 1) * padding
height = rows * cell_h + (rows + 1) * padding + 60

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <style>
    .title {{ font: bold 20px "Segoe UI", sans-serif; fill: #58a6ff; }}
    .emoji {{ font: 32px "Apple Color Emoji", "Noto Color Emoji", sans-serif; }}
    .label {{ font: bold 14px "Segoe UI", sans-serif; fill: #e6edf3; }}
    .desc {{ font: 12px "Segoe UI", sans-serif; fill: #8b949e; }}
  </style>
  <text x="{width/2}" y="35" text-anchor="middle" class="title">🏆 GitHub Trophies</text>
'''

for i, (emoji, label, desc) in enumerate(trophies):
    row = i // cols
    col = i % cols
    x = padding + col * (cell_w + padding)
    y = 50 + padding + row * (cell_h + padding)
    
    svg += f'''
    <g transform="translate({x},{y})">
      <rect x="0" y="0" width="{cell_w}" height="{cell_h}" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1"/>
      <text x="{cell_w/2}" y="35" text-anchor="middle" class="emoji">{emoji}</text>
      <text x="{cell_w/2}" y="55" text-anchor="middle" class="label">{label}</text>
      <text x="{cell_w/2}" y="70" text-anchor="middle" class="desc">{desc}</text>
    </g>
    '''

svg += '</svg>'

with open('trophies.svg', 'w') as f:
    f.write(svg)

print(f"Generated {len(trophies)} trophies")
