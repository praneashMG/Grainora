import re

files_to_update = ['portfolio.html', 'home2.html', 'contact.html', 'process.html']

for filename in files_to_update:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if filename == 'portfolio.html':
            content = content.replace('bg-white/10 dark:bg-black/40', 'bg-black/60 dark:bg-black/70')
            content = content.replace('text-gray-300', 'text-gray-200') # slightly brighter for better contrast
        elif filename == 'home2.html':
            content = content.replace('bg-white/10 border', 'bg-black/60 border')
        elif filename == 'contact.html':
            content = content.replace('bg-white/10 backdrop-blur-md', 'bg-black/60 backdrop-blur-md')
        elif filename == 'process.html':
            content = content.replace('bg-white/10 dark:bg-black/30', 'bg-black/60 dark:bg-black/70')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

