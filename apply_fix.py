with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('shadow-lg flex-1 md:w-1/2 lg:w-full', 'shadow-lg w-full md:flex-1 lg:flex-none')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed flex-1 stretching on Right Column.")
