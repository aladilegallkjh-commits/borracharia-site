import re
with open(r"C:\Users\trevotech\.gemini\antigravity\scratch\borracharia\assets\index-C88p56Dd.js", 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'className:"([^"]+)",children:"Não Perca Tempo"', text)
if match:
    print("Found class:", match.group(1))
else:
    print("Not found")
