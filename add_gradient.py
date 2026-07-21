import os
import subprocess

assets_dir = r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia\assets"
js_file = os.path.join(assets_dir, "index-C88p56Dd.js")
css_file = os.path.join(assets_dir, "index-GkIOROAX.css")

# Update JS
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

js_content = js_content.replace(
    'className:"text-red-500",children:"Não Perca Tempo"',
    'className:"text-premium-gradient",children:"Não Perca Tempo"'
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

# Update CSS
gradient_css = """
.text-premium-gradient {
    background: linear-gradient(90deg, #ff416c 0%, #ff4b2b 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    display: inline-block !important;
    font-weight: 900 !important;
    text-shadow: 0px 4px 15px rgba(255, 75, 43, 0.3) !important;
}
"""
with open(css_file, 'a', encoding='utf-8') as f:
    f.write(gradient_css)

print("Pushing to GitHub...")
os.chdir(r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Adicionar degrade premium no texto principal"])
subprocess.run(["git", "push"])
print("Complete.")
