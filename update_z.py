import re

with open('process.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('opacity-50 z-0 pointer-events-none', 'opacity-50 z-20 pointer-events-none')

with open('process.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated z-index to 20")
