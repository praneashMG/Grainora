with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<div class="flex flex-col md:flex-row lg:flex-col gap-6 lg:col-span-1 h-full">',
    '<div class="flex flex-col md:flex-row lg:flex-col gap-6 lg:col-span-1">'
)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed h-full from right column wrapper.")
