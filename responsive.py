import re

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the grid container
content = content.replace(
    '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-7xl mx-auto">',
    '<div class="grid grid-cols-1 lg:grid-cols-3 gap-6 max-w-7xl mx-auto">'
)

# Replace the large feature item wrapper
content = content.replace(
    '<div class="md:col-span-2 relative group rounded-3xl overflow-hidden h-[400px] md:h-[600px] shadow-lg">',
    '<div class="lg:col-span-2 relative group rounded-3xl overflow-hidden h-[400px] md:h-[500px] lg:h-[600px] shadow-lg">'
)

# Replace the small items wrapper
content = content.replace(
    '<div class="flex flex-col gap-6 md:col-span-1 h-full">',
    '<div class="flex flex-col md:flex-row lg:flex-col gap-6 lg:col-span-1 h-full">'
)

# Replace the small items' height (replace both occurrences using regex or simple replace)
content = content.replace(
    'h-[250px] md:h-[288px] shadow-lg flex-1',
    'h-[250px] md:h-[300px] lg:h-[288px] shadow-lg flex-1 md:w-1/2 lg:w-full'
)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated responsiveness for Bento grid.")
