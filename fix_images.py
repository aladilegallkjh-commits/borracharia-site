import os
import re
import shutil
import subprocess

# Paths
artifact_dir = r"C:\Users\trevotech\.gemini\antigravity\brain\a84eeb8d-84f0-4e87-a1d3-46f5569d5fc9"
assets_dir = r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia\assets"
js_file = os.path.join(assets_dir, "index-C88p56Dd.js")

# Images mapping
images = {
    "service_moto_1784652777253.png": "service_moto.png",
    "service_car_1784652787652.png": "service_car.png",
    "service_truck_1784652804100.png": "service_truck.png",
    "service_rescue_1784652815805.png": "service_rescue.png",
    "service_exchange_1784652828851.png": "service_exchange.png",
    "service_mobile_1784652837850.png": "service_mobile.png"
}

print("Copying images...")
for old, new in images.items():
    src = os.path.join(artifact_dir, old)
    dst = os.path.join(assets_dir, new)
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"Copied {new}")
    else:
        print(f"File not found: {src}")

print("Updating JS file...")
with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'(title:"Borracharia de Moto"[^}]*image:)"assets/[^"]*"', r'\1"assets/service_moto.png"', content)
content = re.sub(r'(title:"Borracharia de Ve[^"]*culo"[^}]*image:)"assets/[^"]*"', r'\1"assets/service_car.png"', content)
content = re.sub(r'(title:"Borracharia de Caminh[^"]*o"[^}]*image:)"assets/[^"]*"', r'\1"assets/service_truck.png"', content)
content = re.sub(r'(title:"Auto Socorro"[^}]*image:)"assets/[^"]*"', r'\1"assets/service_rescue.png"', content)
content = re.sub(r'(title:"Troca de Pneus"[^}]*image:)"assets/[^"]*"', r'\1"assets/service_exchange.png"', content)
content = re.sub(r'(title:"Borracharia M[^"]*vel"[^}]*image:)"assets/[^"]*"', r'\1"assets/service_mobile.png"', content)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Pushing to GitHub...")
os.chdir(r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Adicionar imagens especificas para cada servico geradas por IA"])
subprocess.run(["git", "push"])
print("Complete.")
