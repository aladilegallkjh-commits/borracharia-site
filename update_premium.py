import re
import subprocess
import os

assets_dir = r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia\assets"
js_file = os.path.join(assets_dir, "index-C88p56Dd.js")
css_file = os.path.join(assets_dir, "index-GkIOROAX.css")

# 1. Update text in JS
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Encode to handle potential unicode escapes if needed, but simple replace usually works for UTF-8 files
js_content = js_content.replace('Seu Pneu Furado', 'Seu Pneu Furou?')
js_content = js_content.replace('Não Pode Esperar', 'Não Perca Tempo')
js_content = js_content.replace('Você Pode Confiar', 'Chegamos até Você em Minutos')

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

# 2. Update CSS font to Outfit
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace any font-family with Outfit
css_content = re.sub(r'font-family:[^;}]+', 'font-family: "Outfit", sans-serif', css_content)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 3. Update index.html to load Outfit font
html_file = r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace('<link href="assets/fonts.css" rel="stylesheet">', '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap" rel="stylesheet">')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Pushing to GitHub...")
os.chdir(r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Atualizar texto e fonte para premium (Outfit)"])
subprocess.run(["git", "push"])
print("Complete.")
