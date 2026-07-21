import os
import subprocess

assets_dir = r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia\assets"
js_file = os.path.join(assets_dir, "index-C88p56Dd.js")

# Update JS
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

js_content = js_content.replace(
    'className:"text-premium-gradient"',
    'className:"text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-pink-500 to-orange-500"'
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Pushing to GitHub...")
os.chdir(r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Usar classes Tailwind para o degrade de texto"])
subprocess.run(["git", "push"])
print("Complete.")
