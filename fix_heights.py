import re

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Left Column
# Top Card: lg:h-[400px] -> lg:h-96  (384px)
content = content.replace('h-[300px] md:h-[400px] lg:h-[400px]', 'h-72 md:h-96 lg:h-96')
# Bottom Card: lg:h-[176px] -> lg:h-48 (192px)
content = content.replace('h-[200px] md:h-[200px] lg:h-[176px]', 'h-48 md:h-48 lg:h-48')

# Fix Right Column
# Top and Bottom Cards: lg:h-[288px] -> lg:h-72 (288px)
content = content.replace('h-[250px] md:h-[300px] lg:h-[288px]', 'h-64 md:h-72 lg:h-72')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated to standard Tailwind height classes.")
